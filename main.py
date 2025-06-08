# Imports
import yfinance as yf
import pandas as pd
import numpy
import scipy.optimize
import matplotlib.pyplot

# Constants
riskfree_rate_df = yf.download('^IRX', period='1mo',) # 13 week treasury risk free rate (basis)
tickers_df = pd.read_csv('ticker_data.csv', index_col=0) # Test dataset before I implement actual inputs + downloading yfinance data

# Key variables
riskfree_rate = 0

# Creating dataframe of returns by finding the percentage change from before to now
returns_df = tickers_df.pct_change()

# Deleting all the NaN values that come up in the first row because there is nothing to divide against
returns_df = tickers_df.pct_change().dropna() 

# Finding Expected return using the mean of all historical returns
expected_returns_series = returns_df.mean()

# Getting the risk free rate
riskfree_rate_df = riskfree_rate_df['Close']
riskfree_rate = riskfree_rate_df.iloc[-1] * 100

# Test Output
print(riskfree_rate_df.head())
print(riskfree_rate)
print(returns_df.head())
print(expected_returns_series)