"""
Script to create simplifies Ames house data set with fewer features,
fewer values for categorical variables and metric units.
"""

import numpy as np
import pandas as pd
import csv

from sklearn.datasets import fetch_openml
ds = fetch_openml(name='house_prices')

# Initial set of features to keep
features = [
    'LotArea',
    'Neighborhood',
    'BldgType',
    'OverallQual',
    'OverallCond',
    'YearBuilt',
    'CentralAir',
    'GrLivArea',
    'FullBath',
    'BedroomAbvGr',
    'Fireplaces',
    'GarageType'
 ]

target = 'SalePrice'

# Merge into single DataFrame
df = ds.data[features]
df_target = ds.target.to_frame(target)

# Merge target and features
df = pd.concat((df_target, df), axis=1)

renames = {
    'GrLivArea': 'LivingArea',
    'FullBath': 'Bathrooms',
    'BedroomAbvGr': 'Bedrooms',
    'BldgType': 'BuildingType',
    'OverallQual': 'OverallQuality',
    'OverallCond': 'OverallCondition'
}

df = df.rename(columns=renames)

# Dummy for whether house has any garage
df['HasGarage'] = (df['GarageType'] != 'NA').astype(np.uint8)
del df['GarageType']

# Convert to nicer building type strings
mapping = {
    '1Fam': 'Single-family',
    '2FmCon': 'Two-family',
    'Duplex': 'Two-family',
    'TwnhsE': 'Townhouse',
    'TwnhsI': 'Townhouse'
}

df['BuildingType'] = df['BuildingType'].map(mapping)

# Convert selected columns to integer
columns = ['OverallQuality', 'OverallCondition', 
    'YearBuilt', 'Bathrooms', 
    'Bedrooms', 'Fireplaces'
]

for column in columns:
    df[column] = df[column].astype(int)


# Convert square feet to square meters
columns = ['LivingArea', 'LotArea']
for column in columns:
    df[column] /= 3.281**2.0


print(df)

df.to_csv('data/ames_houses.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)