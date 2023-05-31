"""
Implementation of VFI algorithms with deterministic labour income.
"""

import numpy as np

from scipy.optimize import minimize_scalar
from scipy.interpolate import interp1d

from time import perf_counter


def vfi_grid(par, tol=1e-5, maxiter=1000):
    """
    Solve the household problem using VFI with grid search.

    Parameters
    ----------
    par : Parameters
        Model parameters and grids
    tol : float, optional
        Termination tolerance
    maxiter : int, optional
        Max. number of iterations

    Returns
    -------
    vfun : np.ndarray
        Array containing the value function
    pfun_sav : np.ndarray
        Array containing the savings policy function
    """

    # Keep track of time
    t0 = perf_counter()

    N_a = len(par.grid_a)
    vfun = np.zeros(N_a)
    vfun_upd = np.empty(N_a)
    # index of optimal savings decision (stored in integer array!)
    pfun_isav = np.empty(N_a, dtype=np.uint)

    # pre-compute cash at hand for each asset grid point
    cah = (1 + par.r) * par.grid_a + par.y

    for it in range(maxiter):

        for ia, a in enumerate(par.grid_a):

            # find all values of a' that are feasible, ie. they satisfy
            # the budget constraint
            ia_to = np.where(par.grid_a <= cah[ia])[0]

            # consumption implied by choice a'
            #   c = (1+r)a + y - a'
            cons = cah[ia] - par.grid_a[ia_to]

            # Evaluate "instantaneous" utility
            if par.gamma == 1.0:
                u = np.log(cons)
            else:
                u = (cons**(1.0 - par.gamma) - 1.0) / (1.0 - par.gamma)

            # 'candidate' value for each choice a'
            v_cand = u + par.beta * vfun[ia_to]

            # find the 'candidate' a' which maximizes utility
            ia_to_max = np.argmax(v_cand)

            # store results for next iteration
            vopt = v_cand[ia_to_max]
            vfun_upd[ia] = vopt
            pfun_isav[ia] = ia_to_max

        diff = np.max(np.abs(vfun - vfun_upd))

        # switch references to value functions for next iteration
        vfun, vfun_upd = vfun_upd, vfun

        if diff < tol:
            td = perf_counter() - t0
            msg = f'VFI: Converged after {it:3d} iterations ({td:.1f} sec.): dV={diff:4.2e}'
            print(msg)
            break
        elif it == 1 or it % 10 == 0:
            msg = f'VFI: Iteration {it:3d}, dV={diff:4.2e}'
            print(msg)
    else:
        msg = f'Did not converge in {it:d} iterations'
        print(msg)

    return vfun, pfun_isav


def vfi_interp(par, kind='linear', tol=1e-5, maxiter=1000):
    """
    Solve the household problem using VFI combined with interpolation
    of the continuation value.

    Parameters
    ----------
    par : Parameters
        Model parameters
    kind : str, optional
        Type of interpolation to perform on the continuation value.
    tol : float, optional
        Termination tolerance
    maxiter : int, optional
        Max. number of iterations

    Returns
    -------
    vfun : np.ndarray
        Array containing the value function
    pfun_sav : np.ndarray
        Array containing the savings policy function
    """

    t0 = perf_counter()

    N_a = len(par.grid_a)
    vfun = np.zeros(N_a)
    vfun_upd = np.empty(N_a)
    # Optimal savings decision
    pfun_sav = np.zeros(N_a)

    for it in range(maxiter):

        if kind == 'linear':
            f_vfun = lambda x: np.interp(x, par.grid_a, vfun)
        else:
            # Use any other interpolation that is supported by Scipy's interp1d
            f_vfun = interp1d(
                par.grid_a, vfun, 
                kind=kind, bounds_error=False,
                fill_value='extrapolate', assume_sorted=True,
                copy=False
            )

        for ia, a in enumerate(par.grid_a):
            # Solve maximization problem at given asset level
            # Cash-at-hand at current asset level
            cah = (1.0 + par.r) * a + par.y
            # Restrict maximisation to following interval:
            bounds = (0.0, cah)
            # Arguments to be passed to objective function
            args = (cah, par, f_vfun)
            # perform maximisation
            res = minimize_scalar(f_objective, bracket=bounds, args=args)

            # Minimiser returns NEGATIVE utility, revert that
            vopt = - res.fun
            sav_opt = float(res.x)

            vfun_upd[ia] = vopt
            pfun_sav[ia] = sav_opt

        diff = np.max(np.abs(vfun - vfun_upd))

        # switch references to value functions for next iteration
        vfun, vfun_upd = vfun_upd, vfun

        if diff < tol:
            td = perf_counter() - t0
            msg = f'VFI: Converged after {it:3d} iterations ({td:.1f} sec.): dV={diff:4.2e}'
            print(msg)
            break
        elif it == 1 or it % 10 == 0:
            msg = f'VFI: Iteration {it:3d}, dV={diff:4.2e}'
            print(msg)
    else:
        msg = f'Did not converge in {it:d} iterations'
        print(msg)

    return vfun, pfun_sav


def f_objective(sav, cah, par, f_vfun):
    """
    Objective function for the minimizer.

    Parameters
    ----------
    sav : float
        Current guess for optional savings
    cah : float
        Current CAH level
    par : namedtuple
        Model parameters
    f_vfun : callable
        Function interpolating the continuation value.

    Returns
    -------
    float
        Objective function evaluated at given savings level
    """

    sav = float(sav)
    if sav < 0.0 or sav >= cah:
        return np.inf

    # Consumption implied by savings level
    cons = cah - sav

    # Continuation value interpolated onto asset grid
    vcont = f_vfun(sav)

    # evaluate "instantaneous" utility
    if par.gamma == 1.0:
        u = np.log(cons)
    else:
        u = (cons**(1.0 - par.gamma) - 1.0) / (1.0 - par.gamma)

    # Objective evaluated at current savings level
    obj = u + par.beta * vcont

    # We are running a minimiser, return negative of objective value
    return -obj