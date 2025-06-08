# Imports
import yfinance as yf
import pandas as pd
import numpy as np
from scipy.optimize import minimize
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
riskfree_rate = riskfree_rate/12 # Risk free rates are annualised and need to be converted to monthly
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
# portfolio_return = np.dot(weights, expected_returns_array) #weighted returns cause that's how we 'optimise' the portfolio- kind of the whole point

# Portfolio Variance
# portfolio_variance_matrix = np.dot(weights.T, np.dot(cov_matrix.values, weights)) 
# weights.T transposes so the shape of the datasets matches
# portfolio_volatility = np.sqrt(portfolio_variance_matrix)

# Sharpe Ratio
# Moment of truth...
# sharpe_ratio = (portfolio_return - riskfree_rate)/portfolio_volatility
# negative_sharpe_ratio = -sharpe_ratio

# Optimiser time!
# Blank array of weights for optimiser to fill in values for
num_assets = len(expected_returns_series)
initial_weights = np.array([1/num_assets] * num_assets)

# All weights need to equal to 1 cause the logic is broken otherwise
constraints = ({
    'type': 'eq', # Needs a equality constraint
    'fun': lambda w: np.sum(w) - 1 # Sum of weights needs to equal 1, not less nor more
})

# Limiting range of weights from 0 to 1
bounds = tuple((0, 1) for _ in range(num_assets))


# This is the objective function that needs to be optimised, with the sharpe ratio being the 'y' in this case
def negative_sharpe_ratio(weights, expected_return, cov_matrix, riskfree_rate):
    portfolio_return = np.dot(weights, expected_return)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = (portfolio_return - riskfree_rate) / portfolio_volatility
    return -sharpe_ratio

sharpe_ratio  = -1*negative_sharpe_ratio(weights, expected_returns_array, cov_matrix, riskfree_rate)

result = minimize(
    fun=negative_sharpe_ratio,
    x0=initial_weights,
    args=(expected_returns_array, cov_matrix.values, riskfree_rate),
    method='SLSQP',
    bounds=bounds,
    constraints=constraints
)

optimal_weights = result.x
max_sharpe = -result.fun  # Minimised optimal sharpe

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
# print("Portfolio Return: "  + str(portfolio_return * 100) + "%")
# print("\n")
# print("Portfolio Volatility: "  + str(portfolio_volatility * 100) + "%")
# print("\n")
print("Sharpe Ratio: "  + str(sharpe_ratio))
print("\n")
print("Optimal Weights: " + str(optimal_weights))
print("\n")
print("Optimal Sharpe: " + str(max_sharpe))