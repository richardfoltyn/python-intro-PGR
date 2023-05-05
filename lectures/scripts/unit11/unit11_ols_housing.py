#
# Unit 11: Applications: Econometrics
# 
# This script contains the code for section 3:
#   OLS using housing data

# Directory used to store graphs:
# Use directory where this script is located.
import os
graphdir = os.path.dirname(os.path.abspath(__file__))

# %% 
# ### Complete OLS estimation routine
#
# We reuse the custom OLS function we wrote earlier for this exercise.

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
# ## OLS using housing data
# 
# We now proceed to run a more meaningful regression using the ols() function
# developed above. To this end, we use monthly observations from the
# file HOUSING.csv which contains various variables related to the
# US housing market. In particular, we will take the number of
# housing unit construction starts (variable NHSTART) in a given month
# and regress it on the average sales price of new homes (variable ASPNHS) 
# lagged by 3, 6 and 12 months. 
#
# We run the regression in logs, so the estimated coefficient
# should be interpreted as elasticities.
#
# We first load and inspect the data using pandas.
#
import numpy as np
import pandas as pd

# Determine full path to data file, using the path of the current script
# this is stored in __file__.
import os
datadir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../data')
file = os.path.join(datadir, 'HOUSING.csv')

# Read in CSV data file
df = pd.read_csv(file)

# Inspect first and last rows of the DataFrame
df.head(5)
df.tail(5)

# %% 
# The data contains several variables which we won't be using in this analysis,
# such as the Case-Shiller house price index (CSHPRICE) which has missing
# values for some of the earlier dates (missing values are denoted as `NaN`).
# 
# Let's first plot the bivariate relationship between new house starts and
# the (concurrent) average sales price. The price is in current dollars,
# so we first need to deflate it (using the `CPI`) to make the values 
# comparable across this 45-year period.

import matplotlib.pyplot as plt

# Convert average selling price to 1982-1984 dollars.
# The value of 100 corresponds to the average price level between 1982-1984.
df['ASPNHS'] /= df['CPI'] / 100.0

df.plot.scatter('NHSTART', 'ASPNHS', linewidths=0.75, color='none',
    edgecolor='steelblue')

# Save figure. gcf() retrieves a handle to the currently active figure.
plt.gcf().savefig(os.path.join(graphdir, 'unit11_ols_housing_scatter.pdf'))

# %% 
# This scatter plot looks somewhat unexpected as there seems to be no clear
# relationship between housing supply and house prices. This might be because
# the relationship has not remained stable over the decades covered by our data.
# 
# To see this more clearly, we bin the time periods into five blocks and
# recreate the plots using different colours:

# Create 5 approximately equally-sized bins based on the calendar year
df['Year_bin'] = pd.cut(df['Year'], bins=5, labels=False)

# Plot each group of years using a different color
fig, ax = plt.subplots(1,1, figsize=(8,6))
colors = ['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00']

# Iterate over bins, plot each one separately
bins = df['Year_bin'].unique()
for bin in bins:
    # Restrict data set to relevant years
    df_i = df.loc[df['Year_bin'] == bin].copy()

    # Extract initial and terminal year of this block
    yfrom, yto = df_i['Year'].min(), df_i['Year'].max()

    ax.scatter(df_i['NHSTART'], df_i['ASPNHS'], 
        label=f'Years {yfrom:.0f}-{yto:.0f}',
        edgecolors=colors[bin], color='none')

ax.set_xlabel('New housing units started (in thousand)')
ax.set_ylabel('Avg. new home sales price (in 1982-84 USD)')
ax.legend()
fig.savefig(os.path.join(graphdir, 'unit11_ols_housing_scatter_colour.pdf'))

# Remove year bin column again
del df['Year_bin']

# %% 
# As you see, our suspicion was correct and there are clear changes across
# the sample of 45 years. At this point we could do something more elaborate,
# but for illustrative purposes we just restrict our analysis to the
# period after the year 2000, where we have an upwards-sloping relationship.
#
# Before we can call the function ols(), we need to pre-process the data
# so that we end up with NumPy arrays (the only type of data our function
# accepts).

# Keep only relevant variables, rest just clutters the DataFrame
varlist = ['Year', 'Month', 'ASPNHS', 'NHSTART']
df = df[varlist].copy()

# Create YYYY-MM date index
df['Date'] = pd.PeriodIndex(year=df['Year'], month=df['Month'], freq='M')
df = df.set_index('Date')

# Create 3-month, 6-month and 12-month lags of house prices
lags = 3, 6, 12
for lag in lags:
    df[f'L{lag}ASPNHS'] = df['ASPNHS'].shift(lag)

# Restrict data to year >= 2000
df = df.loc[df['Year'] >= 2000].copy()

# Drop year, month, these are no longer needed
df = df.drop(columns=['Year', 'Month'])

# Plot first 13 rows, which clearly shows the lagged values
df.head(13)

# %% 
# Now that we have created all the lagged variables, we drop all rows with missing data
# and convert the relevant columns to NumPy arrays.
#
# List of variables to include in model
var_X = [f'L{lag}ASPNHS' for lag in lags]
var_y = 'NHSTART'

# Restrict to relevant variables
df = df[var_X + [var_y]].copy()

# drop all rows with missing observations
df = df.dropna()

# Extract raw data from data frame
X = df[var_X].to_numpy()
y = df[var_y].to_numpy()

# Estimate as elasticity in logs
log_X = np.log(X)
log_y = np.log(y)

# Print first 5 observations
print(log_X[:5])

# %%
# ### Estimating the model
# 
# We are now ready to run the OLS regression.
#
# Run our own ols() function. This returns the coefficient vector and the
# variance-covariance matrix.
coefs, vcv = ols(log_X, log_y, add_const=True)

# Compute standard errors from the VCV matrix
se = np.sqrt(np.diag(vcv))

print(f'Estimated coefficients: {coefs}')
print(f'Standard errors: {se}')
print(f'Number of obs: {len(log_y)}')

# %% 
# ### Running OLS using statsmodels
# 
# As you can imagine, estimating an OLS regression is a common task so
# there are packages which already implement this functionality for you.
# One such package is `statsmodels`, which we will now use to verify our
# results.
#
import statsmodels.api as sm

# Explicitly augment the regressor matrix with a constant
log_X1 = sm.add_constant(log_X)

# Define the linear model
model = sm.OLS(log_y, log_X1)

# Estimate the model
result = model.fit()

# Print a summary of the results
print(result.summary())

