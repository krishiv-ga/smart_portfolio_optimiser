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

# Need % change for expected return calc, curve structure should be the same
returns_df = tickers_df.pct_change()

# Takin out the trash
returns_df = tickers_df.pct_change().dropna() 

# Expected return = historical returns/number of datapoints (aka mean)
expected_returns_series = returns_df.mean()

# Getting the risk free rate
riskfree_rate_df = riskfree_rate_df['Close']
riskfree_rate = riskfree_rate_df.iloc[-1].item()/100 # iloc lets us take the most recent datapoint (last one in the dataset) as the updated riskfree rate
# Using .item() to extraploate only the integer value and not the other random metadata that pandas shovels out


# Test Output
print("\n")
print("Risk Free Rates")
print(riskfree_rate_df.head())
print("\n")
print("% Returns")
print(returns_df.head())
print("\n")
print("E(X) returns")
print(expected_returns_series)
print("\n")
print("Risk free rate: " + str(riskfree_rate))
