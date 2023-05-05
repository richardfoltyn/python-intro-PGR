"""
Unit 8, Exercise 2

Author: Richard Foltyn
"""

import numpy as np
from numpy.random import default_rng
from scipy.stats import truncnorm, norm
import matplotlib.pyplot as plt

################################################################################
# Parameters
mu = 0.0
sigma = 1.0
a = mu - 2*sigma
b = mu + 2*sigma

# Standardised boundaries if underlying non-truncated distr. is
# NOT standard normal
za = (a-mu)/sigma
zb = (b-mu)/sigma

# Method 1: Compute from E[X^2] = Var(X) + E[X]^2
var = truncnorm.var(za, zb, loc=mu, scale=sigma)
mean = truncnorm.mean(za, zb, loc=mu, scale=sigma)
m2_var_mean = var + mean ** 2.0

# Method 2: Compute using moment()
m2 = truncnorm.moment(2, za, zb, loc=mu, scale=sigma)

# Method 3: Compute moment using expect() function
m2_expect = truncnorm.expect(lambda x: x ** 2.0, args=(za, zb),
                             loc=mu, scale=sigma)

# Method 4: Monte Carlo integration


# Function to compute integrand
def f_integrand(x, a, b, mu, sigma):
    # Transform to boundaries required by SciPy's truncnorm
    za = (a - mu) / sigma
    zb = (b - mu) / sigma
    # Evaluate truncated normal PDF
    pdf = truncnorm.pdf(x, za, zb, loc=mu, scale=sigma)
    # Compute integrand x^2 * f(x)
    result = x ** 2.0 * pdf
    return result


# Initialise RNG
rng = default_rng(123)
# Sample size for Monte Carlo integration
Nsample = 50000

# x-values should be uniformly distributed on [a, b]
xsample = rng.uniform(a, b, size=Nsample)
# Alternatively we can also just use equidistant x-values, in
# low-dimensional problems it makes no difference.
# xsample = np.linspace(a, b, Nsamples)

# Evaluate integrand at sampled x-values
integrand = f_integrand(xsample, a, b, mu, sigma)

# Compute size of bounding rectangle:
# the height is taken as the largest realisation of the integrand.
length = b - a
height = np.amax(integrand)
area = height * length
# draw y-values from uniform distribution on [0, height]
ysample = rng.uniform(0, height, size=Nsample)
# Compute fraction of points that are underneath the PDF
frac = np.mean(ysample <= integrand)
integral_MC = frac * area

print(f'Second non-central moment, var + mean^2: {m2_var_mean:.5e}')
print(f'Second non-central moment, moment(): {m2:.5e}')
print(f'Second non-central moment, expect(): {m2_expect:.5e}')
print(f'Second non-central moment, MC integration: {integral_MC:.5e}')


################################################################################
# Plot illustration of how Monte Carlo integration works

fig, ax = plt.subplots(1, 1, figsize=(7, 4.5))

# Plot integrand as function on equidistant x-grid
xvalues = np.linspace(a, b, 100)
integrand = f_integrand(xvalues, a, b, mu, sigma)
ax.plot(xvalues, integrand, c='black', lw=2.0, label='Integrand', zorder=100)

# re-draw (smaller) sample of x, y coordinates for illustration
Nsample = 100
xsample = rng.uniform(a, b, size=Nsample)
ysample = rng.uniform(0, height, size=Nsample)
integrand_sample = f_integrand(xsample, a, b, mu, sigma)
# Identify points that are below integrand
mask = (ysample <= integrand_sample)
# Plot points included in integral
ax.scatter(xsample[mask], ysample[mask], c='steelblue', s=20)
# Plot points NOT included in integral (~ negates a boolean array!)
ax.scatter(xsample[~mask], ysample[~mask], c='darkred', marker='x')

# Create bounding rectangle for MC integration
ax.plot([a, a, b, b, a], [0, height, height, 0, 0], c='blue', ls=':', lw=1.5,
        label='Bounding rectangle', zorder=-10)

# Add labels, etc.
ax.set_xlim((a-0.05*length, b+0.05*length))
ax.set_ylim((-0.05*height, height * 1.15))
ax.set_ylabel(r'$x^2 \cdot f(x)$')
ax.set_xlabel(r'$x$')

ax.legend(loc='upper left', frameon=False, ncol=2)
fig.savefig('unit08_ex2_MC.pdf')
# Store as SVG to be included in Notebook
fig.savefig('unit08_ex2_MC.svg')


################################################################################
# Plot truncated pdf

xvalues_trunc = np.linspace(a, b, 100)
xvalues = np.linspace(a - 0.1*length, b + 0.1*length, 100)
# mass of untruncated normal on interval [a, b]
mass = norm.cdf(b, loc=mu, scale=sigma) - norm.cdf(a, loc=mu, scale=sigma)

pdf = norm.pdf(xvalues, loc=mu, scale=sigma)
# Rescale truncated PDF so that it integrates to 1.0
pdf_trunc = norm.pdf(xvalues_trunc, loc=mu, scale=sigma) / mass

fig, ax = plt.subplots(1, 1, figsize=(5, 3))
ax.plot(xvalues, pdf, label='Normal', c='black', ls='--')
ax.plot(xvalues_trunc, pdf_trunc, label='Trunc. normal', c='red', lw=2.0)
ax.legend()
ax.set_xticks([a, mu, b])
ax.set_xticklabels([r'$a$', r'$\mu$', r'$b$'])
ax.set_ylabel('PDF')
ax.set_yticks([])
fig.tight_layout()
fig.savefig('unit08_ex2_PDF.pdf')
# Store as SVG to be included in Notebook
fig.savefig('unit08_ex2_PDF.svg')
