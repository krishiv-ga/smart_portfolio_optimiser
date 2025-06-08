import pandas as pd
import numpy as np

def get_percent_returns(ticker):
    returns_df = ticker.pct_change().dropna()
    return returns_df

def get_expected_return(returns_df):
    return returns_df.mean() 