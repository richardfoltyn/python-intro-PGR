"""
Main script to solve household problem with risky (stochastic) labour income,
using either VFI + grid search or VFI + interpolation.

Introduction to Python Programming for Economics & Finance, 2023
University of Glasgow

Author: Richard Foltyn
"""

#%% Imports and definitions

import numpy as np

from dataclasses import dataclass

from VFI_risk import vfi_grid, vfi_interp
from EGM_risk import egm
from markov import rouwenhorst, markov_ergodic_dist
from plots import plot_solution

#%% Create model parameters

@dataclass
class Parameters:
    """
    Define object to store model parameters and their default values
    """
    beta = 0.96         # Discount factor
    gamma = 1.0         # Risk aversion
    r = 0.04            # Interest rate
    rho = 0.95          # Autocorrelation of log labour income
    sigma = 0.20        # Conditional standard deviation of log labour income
    grid_a = None       # Asset grid (to be created)
    grid_y = None       # Discretised labour income grid (to be created)
    tm_y = None         # Labour transition matrix (to be created)

par = Parameters()

#%% Create asset grid

# Start + end point for asset grid
a_min = 0.0
a_max = 10.0
# Number of grid points
N_a = 50
# Create asset grid with more points at the beginning
grid_a  = a_min + (a_max - a_min) * np.linspace(0.0, 1.0, N_a)**1.4

# Store asset grid in Parameters object
par.grid_a = grid_a

#%% Create labour grid

# Number of grid points
N_y = 3

# Discretise labour income process
states, tm_y = rouwenhorst(N_y, mu=0.0, rho=par.rho, sigma=par.sigma)

# Ergodic distribution of labour income
edist = markov_ergodic_dist(tm_y)

# State space in levels
grid_y = np.exp(states)

# Normalise states such that unconditional expectation is 1.0
grid_y /= np.dot(edist, grid_y)

# Store labour grid and transition matrix
par.grid_y = grid_y
par.tm_y = tm_y

#%% Solve HH problem using VFI + grid search

vfun, pfun_ia = vfi_grid(par)

# Recover savings policy function from optimal asset indices
pfun_a = par.grid_a[pfun_ia]

# Recover consumption policy function from budget constraint
cah = (1.0 + par.r) * par.grid_a + par.grid_y[:, None]
pfun_c = cah - pfun_a

# Plot results
fig, axes = plot_solution(par, pfun_a, pfun_c, vfun)
# Insert legend
labels = [f'$y={y:.2f}$' for y in par.grid_y]
axes[0].legend(labels, loc='upper left')

# Optionally save graph as PDF
# fig.savefig('solution_risk_vfi.pdf')


#%% Solve HH problem using VFI + interpolation

vfun, pfun_a = vfi_interp(par)

# Recover consumption policy function from budget constraint
cah = (1.0 + par.r) * par.grid_a + par.grid_y[:, None]
pfun_c = cah - pfun_a

# Plot results
fig, axes = plot_solution(par, pfun_a, pfun_c, vfun)
# Insert legend
labels = [f'$y={y:.2f}$' for y in par.grid_y]
axes[0].legend(labels, loc='upper left')

# Optionally save graph as PDF
# fig.savefig('solution_risk_vfi_interp.pdf')

#%% Solve HH problem using EGM

pfun_a, pfun_c = egm(par)

# Plot results
fig, axes = plot_solution(par, pfun_a, pfun_c)
# Insert legend
labels = [f'$y={y:.2f}$' for y in par.grid_y]
axes[0].legend(labels, loc='upper left')

# Optionally save graph as PDF
# fig.savefig('solution_risk_egm.pdf')