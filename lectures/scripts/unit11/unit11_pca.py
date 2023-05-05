#
# Unit 11: Applications: Econometrics
#
# This script contains the code for section 1:
#   Singular Value Decomposition (SVD) and Principal Components Analysis (PCA) 
# 

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

# %%
# ### Example: Bivariate normal
#
# Perform SVD and PCA on a sample of bivariate normal draws.

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng

# Draw a bivariate normal sample using the function we defined above
mu = [0.0, 1.0]         # Vector of means
sigma = [0.5, 1.0]      # Vector of standard deviations
rho = 0.75              # Correlation coefficient
Nobs = 200              # Sample size
X = draw_bivariate_sample(mu, sigma, rho, Nobs)
x1, x2 = X.T

# Scatter plot of sample
plt.scatter(x1, x2, linewidths=0.75, c='none', edgecolors='steelblue')
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.title('Draws from bivariate normal distribution')
plt.tight_layout()
plt.savefig(os.path.join(graphdir, 'unit11_bivariate_scatter.pdf'))

# %% 
# Perform SVD
from numpy.linalg import svd

# svd() returns transposed V!
# We use full_matrices=False to get the compact factorisation, otherwise
# U is 200 x 200.
U, S, Vt = svd(X, full_matrices=False)

# Check that U'U is a 2x2 identity matrix
print("U'U:")
print(U.T @ U)

# Check that V'V = VV' is a 2x2 identity matrix
print("V'V:")
print(Vt.T @ Vt)

# Check that X = U*S*V'
X_svd = U * S @ Vt

# Compute the max. absolute difference to original X
diff = np.amax(np.abs(X - X_svd) )
print(f"Max. absolute difference between X and USV': {diff:.2e}")

# %%
# ### Example: Principal components
#
# To perform the PCA, it is recommended to first demean the data:

# Draw random sample
X = draw_bivariate_sample(mu, sigma, rho, Nobs)

# Demean variables in X
Xmean = np.mean(X, axis=0)

# Matrix Z stores the demeaned variables
Z = X - Xmean[None]

# Apply SVD to standardised values
U, S, Vt = svd(Z, full_matrices=False)

# Compute principal components
PC = U * S          # same as U @ np.diag(S)

# Variance is highest for first component
var_PC = np.var(PC, axis=0, ddof=1)
print(f'Principal component variances: {var_PC}')

# Plot principal components

# Scatter plot of sample
fig, axes = plt.subplots(1, 2, figsize=(10,4))
axes[0].scatter(X[:, 0], X[:, 1], linewidths=0.75, c='none', edgecolors='steelblue')
axes[0].axis('equal')
axes[0].set_xlabel(r'$x_1$')
axes[0].set_ylabel(r'$x_2$')
axes[0].axline(Xmean, Xmean + Vt[0], label='PC1', lw=1.0, c='black', zorder=1)
axes[0].axline(Xmean, Xmean + Vt[1], label='PC2', lw=1.0, c='red', zorder=1)

# Plot principal component axes
PC_arrows = Vt * np.sqrt(var_PC[:, None])
for v in PC_arrows:
    # Scale up arrows by 3 so that they are visible!
    axes[0].annotate('', Xmean + v*3, Xmean, arrowprops=dict(arrowstyle='->', linewidth=2))

axes[0].legend()

# Plot in principal component coordinate system
axes[1].scatter(PC[:, 0], PC[:, 1], linewidths=0.75, c='none', edgecolors='steelblue')
axes[1].set_xlabel('PC1')
axes[1].set_ylabel('PC2')
axes[1].axis('equal')
axes[1].axvline(0.0, lw=1.0, c='red')
axes[1].axhline(0.0, lw=1.0, c='black')

fig.tight_layout()
fig.savefig(os.path.join(graphdir, 'unit11_pca.pdf'))

# %%
# Perform PCA using scikit-learn

from sklearn.decomposition import PCA

# Draw the same sample as before
X = draw_bivariate_sample(mu, sigma, rho, Nobs)

# Create PCA with 2 components (which is the max, since we have only two 
# variables)
pca = PCA(n_components=2)

# Perform PCA on input data
pca.fit(X)

# The attribute components_ can be used to retrieve the V' matrix
print("Principal components (matrix V'):")
print(pca.components_)

# The attribute explained_variance_ stores the variances of all PCs
print(f'Variance of each PC: {pca.explained_variance_}')

# Fraction of variance explained by each component:
print(f'Fraction of variance of each PC: {pca.explained_variance_ratio_}')
