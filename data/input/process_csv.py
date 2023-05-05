"""
Script to import single data series from FRED (or other sources, but identical
format) and process them into data sets used for the course.

Author: Richard Foltyn
"""

import os

import numpy as np
import pandas as pd

mypath = os.path.abspath(__file__)

# Directory of current script file
basedir = os.path.dirname(mypath)

indir = os.path.join(basedir, 'CSV')
outdir = os.path.abspath(os.path.join(basedir, '..'))


def import_series(path, start=None, stop=None, varname=None, freq=None,
                  transform='mean'):
    """
    Import and transport single series from FRED CSV file.

    Parameters
    ----------
    path : str
        Path to CSV file containing series data exported from FRED
    start : int, optional
        Drop data prior to given year
    stop : int, optional
        Drop data after given year
    varname : str, optional
        If not None, rename variable to given name
    freq : str, optional
        If not None, transform to given time frequency
    transform : str or callable, optional
        Specify function used to transform to different time frequency
        (mean, first, last, etc.)

    Returns
    -------
    df : pd.DataFrame
    """

    df = pd.read_csv(path, sep=',', parse_dates=['DATE'])

    # determine name of column other than DATE
    oldname = set(df.columns) - {'DATE'}
    if len(oldname) != 1:
        raise ValueError('More than one data column in DataFrame')
    oldname = oldname.pop()

    if varname is not None:
        # rename variable name
        df.rename(columns={oldname: varname}, inplace=True)
    else:
        varname = oldname

    date = pd.DatetimeIndex(df['DATE'])

    # Filter out unwanted years, if applicable;
    # default: include all data points
    mask = np.ones(len(date), dtype=bool)

    # Apply start year restriction
    if start is not None:
        mask[date.year < start] = False

    # Apply terminal year restriction
    if stop is not None:
        mask[date.year > stop] = False

    if start is not None or stop is not None:
        df = df.loc[mask, :].copy()
        # Recreate date so they are of equal length
        date = pd.DatetimeIndex(df['DATE'])

    if freq is not None:
        # validate input, map to canonical freq names 'month', 'quarter', 'year'
        freq = freq.lower()
        # allow for some common variants, map to canonical names
        freq_map = {'monthly': 'month', 'quarterly': 'quarter',
                    'annual': 'year', 'annually': 'year'}
        freq = freq_map.get(freq, freq)
        # At this point the value should be one of these three valid strings
        valid = ['month', 'quarter', 'year']
        if freq not in valid:
            s = ', '.join(valid)
            raise ValueError(f'Invalid freq argument. Valid values: {s}')

        # Create grouping based on desired frequency
        if freq == 'month':
            df['Month'] = date.month
            df['Year'] = date.year
            grp = df.groupby(['Year', 'Month'])
        elif freq == 'quarter':
            df['Quarter'] = date.quarter
            df['Year'] = date.year
            grp = df.groupby(['Year', 'Quarter'])
        else:
            # annual data
            df['Year'] = date.year
            grp = df.groupby(['Year'])

        # apply aggregation. This should not do anything for mean, first,
        # and last functions if the original data already has the
        # desired frequency.
        df = grp.agg({'DATE': 'first', varname: transform})

    return df


def combine_series(indir, series, start=None, stop=None, freq=None,
                   transform='mean'):
    """
    Import, transform and combine multiple series from FRED stored in CSV
    format.

    Parameters
    ----------
    indir : str
        Input directory containing CSV files exported from FRED
    series : dict
        Mapping of output series names to FRED series names.
        If FRED series name is None, the output series name is used.
    start : int, optional
        Drop data prior to given year
    stop : int, optional
        Drop data after given year
    freq : str, optional
        If not None, transform to given time frequency
    transform : str or callable, optional
        Specify function used to transform to different time frequency
        (mean, first, last, etc.)

    Returns
    -------
    pd.DataFrame
        DataFrame containing all requested series.
    """

    df_all = None

    for key, name in series.items():
        # if name is None then the name of the input series is the
        # same as the name of the output series, which is key here.
        name = key if not name else name
        fn = os.path.join(indir, f'{name}.csv')

        varname = key
        df = import_series(fn, start, stop, varname, freq, transform)

        if df_all is None:
            df_all = df
        else:
            if 'DATE' in df.columns:
                del df['DATE']
            df_all = df_all.join(df)

    return df_all


################################################################################
# Create minimal annual FRED data set

series = {'GDP': 'GDPC1', 'CPI': 'CPIAUCSL', 'UNRATE': None}

df = combine_series(indir, series, start=1948, stop=2019, freq='annual')

# Round to 1 decimal digits
df = df.round(1)

# Drop DATE
del df['DATE']

fn = os.path.join(outdir, 'FRED.csv')
df.to_csv(fn, index=True, sep=',')

################################################################################
# FRED data set with more series, quarterly frequency

series = {'GDP': 'GDPC1', 'CPI': 'CPIAUCSL', 'UNRATE': None,
          'LFPART': 'CIVPART', 'GDPPOT': None, 'NROU': None}

df = combine_series(indir, series, start=1948, stop=2019, freq='quarter')

# Round to 1 decimal digits
df = df.round(1)

# Drop DATE
del df['DATE']

fn = os.path.join(outdir, 'FRED_QTR.csv')
df.to_csv(fn, index=True, sep=',')


################################################################################
# FRED data related to housing

series = {
    'NHSTART': 'HOUST',
    'MORTGAGE30': 'MORTGAGE30US',
    'CSHPRICE': 'CSUSHPISA',
    'HSN1F': 'HSN1F',
    'ASPNHS': 'ASPNHSUS',
    'CPI': 'CPIAUCSL',
    'HSUPPLY': 'MSACSR'
}

df = combine_series(indir, series, start=1975, stop=2021, freq='month')

# Round to 1 decimal digits
df = df.round(1)

# Drop DATE
del df['DATE']

fn = os.path.join(outdir, 'HOUSING.csv')
df.to_csv(fn, index=True, sep=',')

