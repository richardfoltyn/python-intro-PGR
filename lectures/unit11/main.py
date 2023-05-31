"""
Main script to solve household problem with deterministic labour income,
using either VFI + grid search or VFI + interpolation.
"""

#%% Imports and definitions

import numpy as np

from dataclasses import dataclass

from VFI import vfi_grid, vfi_interp
from plots import plot_solution

#%% Create model parameters

@dataclass
class Parameters:
    """
    Define object to store model parameters and their default values
    """
    beta = 0.96
    gamma = 1.0
    y = 1.0
    r = 0.04
    grid_a = None

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

#%% Solve HH problem using VFI + grid search

vfun, pfun_ia = vfi_grid(par)

# Recover savings policy function from optimal asset indices
pfun_a = par.grid_a[pfun_ia]

# Recover consumption policy function from budget constraint
cah = (1.0 + par.r) * par.grid_a + par.y
pfun_c = cah - pfun_a

# Plot results
fig, axes = plot_solution(par, pfun_a, pfun_c, vfun)
# Optionally save graph as PDF
# fig.savefig('solution.pdf')


#%% Solve HH problem using VFI + grid search

vfun, pfun_a = vfi_interp(par)

# Recover consumption policy function from budget constraint
cah = (1.0 + par.r) * par.grid_a + par.y
pfun_c = cah - pfun_a

# Plot results
fig, axes = plot_solution(par, pfun_a, pfun_c, vfun)
# Optionally save graph as PDF
# fig.savefig('solution_interp.pdf')

