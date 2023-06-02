"""
Common plotting routines

Introduction to Python Programming for Economics & Finance, 2023
University of Glasgow

Author: Richard Foltyn
"""


import matplotlib.pyplot as plt
import numpy as np

def plot_solution(par, pfun_a, pfun_c, vfun=None, xlim=None):
    """
    Plot solution to household problem.

    Parameters
    ----------
    par : Parameters
        Parameters object
    pfun_a : np.ndarray
        Array containing savings policy function
    pfun_c : np.ndarray
        Array containing consumption policy function
    vfun : np.ndarray, optional
        Array containing value function. The default is None.
    xlim : tuple, optional
        Plot limits for x-axis. The default is None.

    Returns
    -------
    fig : 
        Matplotlib figure object
    axes : np.ndarray
        Array of Axes objects

    """

    # Number of columns
    ncols = 3 if vfun is not None else 2

    fig, axes = plt.subplots(
        nrows=1, ncols=ncols, 
        sharex=True, sharey=False, 
        figsize=(3*ncols, 3.5)
    )

    # Restrict to desired domain
    if xlim is not None:
        imax = np.where(par.grid_a > xlim[-1])[0][0] + 1
        xvalues = par.grid_a[:imax]
    else:
        imax = len(par.grid_a)
        xvalues = par.grid_a
        
    # Common style settings
    style = {
        'lw': 2.0,
        'alpha': 0.7
    }
    
    # Common grid settings
    grid = {
        'visible': True,
        'lw': 0.5,
        'ls': ':',
        'zorder': -100,
        'alpha': 0.3,
        'color': 'black'
    }

    # Plot savings
    axes[0].plot(xvalues, pfun_a[..., :imax].T, **style)
    axes[0].set_title(r'Savings $a^{\prime}$')
    axes[0].set_xlabel('Assets')
    axes[0].set_xlim(xlim)
    axes[0].grid(**grid)
    
    # Plot consumption
    axes[1].plot(xvalues, pfun_c[..., :imax].T, **style)
    axes[1].set_title(r'Consumption $c$')
    axes[1].set_xlabel('Assets')
    axes[1].set_xlim(xlim)
    axes[1].grid(**grid)

    # Plot value function, if present
    if vfun is not None:    
        axes[2].plot(xvalues, vfun[..., :imax].T, **style)
        axes[2].set_title('Value func. $V$')
        axes[2].set_xlabel('Assets')
        axes[2].set_xlim(xlim)
        axes[2].grid(**grid)

    fig.tight_layout()

    return fig, axes