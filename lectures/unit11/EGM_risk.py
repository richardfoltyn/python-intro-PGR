"""
Solve household problem with risky labour income using the endogenous
grid-point method (EGM).

Introduction to Python Programming for Economics & Finance, 2023
University of Glasgow

Author: Richard Foltyn
"""

from time import perf_counter
import numpy as np
from scipy.interpolate import interp1d



def egm(par, tol=1.0e-8, maxiter=10000):
    """
    Solve infinite-horizon problem with stochastic labour income using EGM.

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
    pfun_a : np.ndarray
        Savings policy function defined on beginning-of-period asset grid.    
    pfun_c : np.ndarray
        Consumption policy function defined on beginning-of-period asset grid.
    """

    t0 = perf_counter()

    N_a, N_y = len(par.grid_a), len(par.grid_y)
    shape = (N_y, N_a)

    # Cash-at-hand at every asset/savings level
    cah = (1.0 + par.r) * par.grid_a[None] + par.grid_y[:, None]

    # Initial guess for consumption policy function
    pfun_c = np.copy(cah)
    pfun_c_upd = np.zeros(shape)

    # Extract parameters from par object
    beta, gamma, r = par.beta, par.gamma, par.r

    for it in range(maxiter):

        # Iterate over all labour income states
        for iy, y in enumerate(par.grid_y):

            # Expected marginal utility tomorrow
            mu = np.dot(par.tm_y[iy], pfun_c**(-gamma))
            # Compute right-hand side of Euler equation (EE)
            ee_rhs = beta * (1.0 + r) * mu

            # Invert EE to get consumption as a function of savings today
            cons_sav = ee_rhs**(-1.0/gamma)

            # Use budget constraint to get beginning-of-period assets
            assets_sav = (cons_sav + par.grid_a - y) / (1.0 + r)

            # Interpolate back onto exogenous savings grid
            f_cons = interp1d(
                assets_sav, cons_sav, 
                copy=False, assume_sorted=True,
                bounds_error=False, fill_value='extrapolate'
            )
            pfun_c_upd[iy] = f_cons(par.grid_a)

            # Fix consumption in region where HH does not save
            amin = assets_sav[0]
            idx = np.where(par.grid_a <= amin)[0]
            # HH consumes entire cash-at-hand
            pfun_c_upd[iy, idx] = cah[iy, idx]

        # Make sure that consumption policy satisfies constraints
        assert np.all(pfun_c_upd >= 0.0) and np.all(pfun_c_upd <= cah)

        # Compute max. absolute difference to policy function from previous
        # iteration.
        diff = np.max(np.abs(pfun_c - pfun_c_upd))

        # switch references to policy functions for next iteration
        pfun_c, pfun_c_upd = pfun_c_upd, pfun_c

        if diff < tol:
            # Convergence achieved, exit loop
            td = perf_counter() - t0
            msg = f'EGM: Converged after {it:d} iterations ({td:.3f} sec.): ' \
                  f'd(c)={diff:4.2e}'
            print(msg)
            break
        elif it == 1 or it % 10 == 0:
            msg = f'EGM: Iteration {it:4d}, dV={diff:4.2e}'
            print(msg)
    else:
        msg = f'Did not converge in {it:d} iterations'
        print(msg)

    pfun_a = cah - pfun_c

    return pfun_a, pfun_c
