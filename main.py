# Imports
import yfinance
import pandas as pd
import numpy
import scipy.optimize
import matplotlib.pyplot

# Constants

# Key variables

# Taking Ticker Data 
tickers_df = pd.read_csv('ticker_data.csv', index_col=0)

# Creating dataframe of returns by finding the percentage change from before to now
returns_df = tickers_df.pct_change()
# Deleting all the NaN values that come up in the first row because there is nothing to divide against
returns_df = tickers_df.pct_change().dropna() 

# Finding Expected return
expected_returns_series = returns_df.mean()

# Test Output
print(returns_df.head())
print(expected_returns_series)