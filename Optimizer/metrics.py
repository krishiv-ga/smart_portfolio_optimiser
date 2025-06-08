import pandas as pd
import numpy as np

def get_percent_returns(ticker):
    returns_df = ticker.pct_change().dropna()
    return returns_df

def get_expected_return(returns_df):
    return returns_df.mean() 

def get_volatility(returns, expected_returns):
    deviations = returns - expected_returns 
    deviations_squared = deviations ** 2 
    sum_of_deviations_squared = deviations_squared.sum()
    volatility = np.sqrt(sum_of_deviations_squared / len(deviations_squared.index)) 
    return volatility

def get_covariance(returns):
    return returns.cov()

def get_number_of_assets(returns):
    return len(returns)