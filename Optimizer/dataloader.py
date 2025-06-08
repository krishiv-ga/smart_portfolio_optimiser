import yfinance as yf
import pandas as pd
import numpy as np

# Importing Ticker data
# Sample test until proper yf ticker filtering is implemented
def import_ticker():
    return pd.read_csv('Optimizer/ticker_data.csv', index_col=0)

def import_riskfree_rate():
    riskfree_rate_df = yf.download('^IRX', period='1mo') # 13 week treasury bills, annualised
    riskfree_rate_df = riskfree_rate_df['Close'] # We only want the closing rates
    riskfree_rate = riskfree_rate_df.iloc[-1].item() # Latest risk free rate (at the end of the dataset, -1)
    riskfree_rate = riskfree_rate/(12*100)
    return riskfree_rate