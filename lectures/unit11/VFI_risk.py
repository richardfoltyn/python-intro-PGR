"""
Implementation of VFI algorithms with risky labour income.

Introduction to Python Programming for Economics & Finance, 2023
University of Glasgow

Author: Richard Foltyn
"""

import numpy as np

from scipy.optimize import minimize_scalar
from scipy.interpolate import interp1d

from time import perf_counter


def vfi_grid(par, tol=1e-5, maxiter=1000):
    """
    Solve the household problem with risky labour income using VFI with grid
    search.

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
    pfun_ia : np.ndarray
        Array containing the indices of optimal next-period assets a'
    """

    # Keep track of time
    t0 = perf_counter()

    N_a, N_y = len(par.grid_a), len(par.grid_y)
    shape = (N_y, N_a)
    vfun = np.zeros(shape)
    vfun_upd = np.empty(shape)
    # index of optimal savings decision (stored in integer array!)
    pfun_ia = np.empty(shape, dtype=np.uint)

    # pre-compute cash at hand for each (labour, asset) grid point
    cah = (1 + par.r) * par.grid_a[None] + par.grid_y[:,None]

    for it in range(maxiter):

        # Compute expected continuation value E[V(y',a')|y] for each (y,a')
        EV = np.dot(par.tm_y, vfun)

        for iy in range(N_y):
            for ia, a in enumerate(par.grid_a):

                # find all values of a' that are feasible, ie. they satisfy
                # the budget constraint
                ia_to = np.where(par.grid_a <= cah[iy, ia])[0]

                # consumption implied by choice a'
                #   c = (1+r)a + y - a'
                cons = cah[iy, ia] - par.grid_a[ia_to]

                # Evaluate "instantaneous" utility
                if par.gamma == 1.0:
                    u = np.log(cons)
                else:
                    u = (cons**(1.0 - par.gamma) - 1.0) / (1.0 - par.gamma)

                # 'candidate' value for each choice a'
                v_cand = u + par.beta * EV[iy, ia_to]

                # find the 'candidate' a' which maximizes utility
                ia_to_max = np.argmax(v_cand)

                # store results for next iteration
                vopt = v_cand[ia_to_max]
                vfun_upd[iy, ia] = vopt
                pfun_ia[iy, ia] = ia_to_max

        diff = np.max(np.abs(vfun - vfun_upd))

        # switch references to value functions for next iteration
        vfun, vfun_upd = vfun_upd, vfun

        if diff < tol:
            td = perf_counter() - t0
            msg = f'VFI: Converged after {it:3d} iterations ({td:.3f} sec.): dV={diff:4.2e}'
            print(msg)
            break
        elif it == 1 or it % 10 == 0:
            msg = f'VFI: Iteration {it:3d}, dV={diff:4.2e}'
            print(msg)
    else:
        msg = f'Did not converge in {it:d} iterations'
        print(msg)

    return vfun, pfun_ia


def vfi_interp(par, tol=1e-5, maxiter=1000):
    """
    Solve the household problem using VFI combined with interpolation
    of the continuation value.

    Parameters
    ----------
    par : Parameters
        Model parameters
    tol : float, optional
        Termination tolerance
    maxiter : int, optional
        Max. number of iterations

    Returns
    -------
    vfun : np.ndarray
        Array containing the value function
    pfun_a : np.ndarray
        Array containing the savings policy function
    """

    t0 = perf_counter()

    N_a, N_y = len(par.grid_a), len(par.grid_y)
    shape = (N_y, N_a)
    vfun = np.zeros(shape)
    vfun_upd = np.empty(shape)
    # Optimal savings decision
    pfun_a = np.zeros(shape)

    for it in range(maxiter):

        # Compute expected continuation value E[V(y',a')|y] for each (y,a')
        EV = np.dot(par.tm_y, vfun)

        for iy, y in enumerate(par.grid_y):

            # function to interpolate continuation value
            f_vfun = lambda x: np.interp(x, par.grid_a, EV[iy])
            # Alternative interpolation method:
            # f_vfun = interp1d(par.grid_a, EV[iy], assume_sorted=True, 
            #                   copy=False, bounds_error=False,
            #                   fill_value='extrapolate',
            #                   kind='quadratic')

            for ia, a in enumerate(par.grid_a):
                # Solve maximization problem at given asset level
                # Cash-at-hand at current asset level
                cah = (1.0 + par.r) * a + y
                # Restrict maximisation to following interval:
                bounds = (0.0, cah)
                # Arguments to be passed to objective function
                args = (cah, par, f_vfun)
                # perform maximisation
                res = minimize_scalar(f_objective, bracket=bounds, args=args)

                # Minimiser returns NEGATIVE utility, revert that
                vopt = - res.fun
                sav_opt = float(res.x)

                vfun_upd[iy, ia] = vopt
                pfun_a[iy, ia] = sav_opt

        diff = np.max(np.abs(vfun - vfun_upd))

        # switch references to value functions for next iteration
        vfun, vfun_upd = vfun_upd, vfun

        if diff < tol:
            td = perf_counter() - t0
            msg = f'VFI: Converged after {it:3d} iterations ({td:.3f} sec.): dV={diff:4.2e}'
            print(msg)
            break
        elif it == 1 or it % 10 == 0:
            msg = f'VFI: Iteration {it:3d}, dV={diff:4.2e}'
            print(msg)
    else:
        msg = f'Did not converge in {it:d} iterations'
        print(msg)

    return vfun, pfun_a


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