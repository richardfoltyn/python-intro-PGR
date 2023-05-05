#
# Unit 11: Applications: Econometrics
# 
# This script contains the code for section 2:
#   Implementing OLS using SVD

# Directory used to store graphs:
# Use directory where this script is located.
import os
graphdir = os.path.dirname(os.path.abspath(__file__))

# %% 
# ## Preliminaries: drawing random samples.
import numpy as np
from numpy.random import default_rng

def draw_bivariate_sample(mean, std, rho, n, seed=123):
    """
    Draw a bivariate normal random sample.

    Parameters
    ----------
    mean : array_like
        Length-2 array of means
    std : array_like
        Length-2 array of standard deviations
    rho : float
        Correlation parameter
    n : int
        Sample size
    """

    if not -1 <= rho <= 1:
        raise ValueError(f'Invalid correlation parameter: {rho}')

    if np.any(np.array(std) <= 0):
        raise ValueError(f'Invalid standard deviation: {std}')

    if n <= 0:
        raise ValueError(f'Invalid sample size: {n}')

    # initialize default RNG with given seed
    rng = default_rng(seed)

    # Unpack standard deviations for each dimension
    std1, std2 = std

    # Compute covariance
    cov = rho * std1 * std2

    # Create variance-covariance matrix
    vcv = np.array([[std1**2.0, cov],
                    [cov, std2**2.0]])

    # Draw MVN random numbers:
    # each row represents one sample draw.
    X = rng.multivariate_normal(mean=mean, cov=vcv, size=n)

    return X

# ## Ordinary least squares (OLS)

# %% 
# ### Example 1: Bivariate data
#
# Compute the OLS estimator using the formula
#
#   beta = Cov(y,x)/Var(x)
#
import numpy as np
import matplotlib.pyplot as plt

mu = [-1.0, 1.0]                # Mean of X and Y
std = [0.5, 1.5]                # Std. dev. of X and Y
rho = -0.5                      # Correlation coefficient
Nobs = 100                      # Sample size

# We transpose the return value and unpack individual rows into X and Y
x, y = draw_bivariate_sample(mu, std, rho, Nobs).T

# Compute beta (slope coefficient) from distribution moments.
# This is the true underlying relationship given our data generating process.
cov = rho * np.prod(std)
beta = cov / std[0]**2.0
print(f'Slope of population regression line: {beta}')

# Compute beta from sample moments
# Sample variance-covariance matrix (ddof=1 returns the unbiased estimate)
cov_hat = np.cov(x, y, ddof=1)[0, -1]
var_x_hat = np.var(x, ddof=1)
beta_hat = cov_hat / var_x_hat
# Sample intercept
alpha_hat = np.mean(y) - beta_hat * np.mean(x)

print(f'Slope of sample regression line: {beta_hat}')

# Scatter plot of sample
plt.scatter(x, y, linewidths=0.75, c='none', edgecolors='steelblue')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title('Draws from bivariate normal distribution')
plt.axline(mu, slope=beta, color='red', label='Regression line (population)')
plt.axline((0, alpha_hat), slope=beta_hat, color='black', label='Regression line (sample)')
plt.legend()

plt.tight_layout()
plt.savefig(os.path.join(graphdir, 'unit11_ols_impl_regression.pdf'))

# %% 
# ### Example 2: OLS using matrix algebra
#
# #### Naive solution using inverse

from numpy.linalg import inv

# We transpose the return value and unpack individual rows into X and Y
x, y = draw_bivariate_sample(mu, std, rho, Nobs).T

# Create vector of ones (required to estimate the intercept)
ones = np.ones((len(x), 1))
# Prepend constant to vector of regressors to create regressor matrix X
X = np.hstack((ones, x[:, None]))

# Compute inverse of X'X
XXinv = inv(X.T @ X)

print("Explicitly computed (X'X)^(-1):")
print(XXinv)

# Compute naive estimate of gamma
gamma_naive = XXinv @ X.T @ y
print(f'Naive estimate of gamma: {gamma_naive}')

# %%
# #### Solve as a linear equation system

# %%
from numpy.linalg import solve

# Compute X'X
A = X.T @ X
# Compute X'y
b = X.T @ y

# Solve for coefficient vector
gamma_solve = solve(A, b)
print(f'Estimate of gamma using solve(): {gamma_solve}')

# %% 
# #### Solve using NumPy's lstsq()

# %%
from numpy.linalg import lstsq

# Estimate using lstsq(). Pass rcond=None to suppress a warning.
gamma_lstsq, *rest = lstsq(X, y, rcond=None)

print(f'Estimate of gamma using lstsq(): {gamma_lstsq}')

# %%
# ### Example 3: Implementing OLS yourself
#
# Implement using SVD

from numpy.linalg import svd

# Request "compact" SVD, we don't need the full matrix U.
U, S, Vt = svd(X, full_matrices=False)

# Note that S returned by svd() is a vector that contains the diagonal
# of the matrix Sigma.
gamma_svd = Vt.T * S**(-1) @ U.T @ y
print(f'Estimate of gamma using SVD: {gamma_svd}')

# %%
# ### Example 4: OLS standard errors
# 
# Compute standard errors using SVD
#
from numpy.linalg import svd

# Request "compact" SVD, we don't need the full matrix U.
U, S, Vt = svd(X, full_matrices=False)

# Compute point estimate as before
gamma = Vt.T * S**(-1) @ U.T @ y

# Compute (X'X)^-1 
XXinv = Vt.T * S**(-2) @ Vt

# Residuals are given as u = y - X*gamma
residuals = y - X @ gamma

# Variance of residuals
k = X.shape[1]
var_u = np.var(residuals, ddof=k)

# Variance-covariance matrix of estimates
var_gamma = var_u * XXinv

# Standard errors are square roots of diagonal elements of Var(gamma)
gamma_se = np.sqrt(np.diag(var_gamma))

print(f'Point estimate of gamma: {gamma}')
print(f'Standard errors of gamma: {gamma_se}')

# %%
# ### Example 5: Complete OLS estimation routine
#
def ols(X, y, add_const=False):
    """
    Run the OLS regression y = X * beta + u
    and return the estimated coefficients beta and their variance-covariance
    matrix.

    Parameters
    ----------
    X : array_like
        Matrix (or vector) of regressors
    y : array_like
        Vector of observations of dependent variable
    add_const : bool, optional
        If True, prepend a constant to regressor matrix X.
    """

    from numpy.linalg import svd

    # Make sure that y is a one-dimensional array
    y = np.atleast_1d(y)

    # Number of obs.
    Nobs = y.size

    # Make sure that X is a matrix and the leading dimension contains the
    # observations
    X = np.atleast_2d(X).reshape((Nobs, -1))

    # Check that arrays are of conformable dimensions, and raise an exception
    # if that is not the case
    if X.shape[0] != Nobs:
        raise ValueError('Non-conformable arrays X and y')

    # Check whether we need to prepend a constant
    if add_const:
        ones = np.ones((Nobs, 1))
        X = np.hstack((ones, X))

    # Request "compact" SVD, we don't need the full matrix U.
    U, S, Vt = svd(X, full_matrices=False)

    # Compute point estimate using SVD factorisation
    beta = Vt.T * S**(-1) @ U.T @ y

    # Compute (X'X)^-1 using SVD factorisation
    XXinv = Vt.T * S**(-2) @ Vt

    # Residuals are given as u = y - X*beta
    residuals = y - X @ beta

    # Number of model parameters
    k = X.shape[1]

    # Variance of residuals
    var_u = np.var(residuals, ddof=k)

    # Variance-covariance matrix of estimates
    var_beta = var_u * XXinv

    return beta, var_beta

# %%
#
# ### Test our custom OLS function
#

# Draw random sample, split into x and y
x, y = draw_bivariate_sample(mu, std, rho, Nobs).T

# Call OLS estimator. Note that we don't need to manually add a constant!
beta, vcv = ols(x, y, add_const=True)

# Compute standard errors
beta_SE = np.sqrt(np.diag(vcv))

print(f'Point estimate: {beta}')
print(f'Standard errors: {beta_SE}')