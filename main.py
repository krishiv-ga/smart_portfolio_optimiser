# Imports
import yfinance as yf
import pandas as pd
import numpy as np
import scipy.optimize
import matplotlib.pyplot

# Constants
riskfree_rate_df = yf.download('^IRX', period='1mo',) # 13 week treasury risk free rate (basis)
tickers_df = pd.read_csv('ticker_data.csv', index_col=0) # Test dataset before I implement actual inputs + downloading yfinance data

# Key variables
riskfree_rate = 0
portfolio_return = 0
portfolio_volatility = 0


# Need % change for expected return calc, curve structure should be the same
returns_df = tickers_df.pct_change()

# Takin out the trash
returns_df = tickers_df.pct_change().dropna() 

# Expected return = historical returns/number of datapoints (aka mean)
expected_returns_series = returns_df.mean()
expected_returns_array = expected_returns_series.values

# Getting the risk free rate
riskfree_rate_df = riskfree_rate_df['Close']
riskfree_rate = riskfree_rate_df.iloc[-1].item()/100 # iloc lets us take the most recent datapoint (last one in the dataset) as the updated riskfree rate
# Using .item() to extraploate only the integer value and not the other random metadata that pandas shovels out

# Volatility
deviations_df = returns_df - expected_returns_series # Deviation from mean is essential for volatility calculation
deviations_squared_df = deviations_df ** 2 
sum_of_deviations_squared_series = deviations_squared_df.sum()
volatility_series = np.sqrt(sum_of_deviations_squared_series / len(deviations_squared_df.index)) 
# Sum of square deviations by number of items -1 gives us variance, and root of that gives us volatility

# Covariance
cov_matrix = returns_df.cov()

# Swapping to numpy for further calculations due to performance and scipy.optimise compatibility
# Weights
weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])  # Temporary hotfix, will automatically fill by sharpe optimiser based on number of tickers
# TODO: Scale with ticker count rather than be hard coded- also empty cells on defining as optimiser will autofill

# Portfolio Return
portfolio_return = np.dot(weights, expected_returns_array) #weighted returns cause that's how we 'optimise' the portfolio- kind of the whole point

# Portfolio Variance
portfolio_variance_matrix = np.dot(weights.T, np.dot(cov_matrix.values, weights)) 
# weights.T transposes so the shape of the datasets matches
portfolio_volatility = np.sqrt(portfolio_variance_matrix)

# Sharpe Ratio
# Moment of truth...
sharpe_ratio = (portfolio_return - riskfree_rate)/portfolio_volatility

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
print("Deviations")
print(deviations_df.head())
print("\n")
print("Deviations squared")
print(deviations_squared_df.head())
print("\n")
print("Sum of deviations squared")
print(sum_of_deviations_squared_series)
print("\n")
print(volatility_series)
print("\n")
print(cov_matrix)
print("\n")
print("Risk free rate: " + str(riskfree_rate * 100) + "%")
print("\n")
print("Portfolio Return: "  + str(portfolio_return * 100) + "%")
print("\n")
print("Portfolio Volatility: "  + str(portfolio_volatility * 100) + "%")
print("\n")
print("Sharpe Ratio: "  + str(sharpe_ratio))