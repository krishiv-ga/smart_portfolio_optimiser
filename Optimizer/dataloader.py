import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Importing Ticker data
# Sample test until proper yf ticker filtering is implemented
def import_ticker():
    return pd.read_csv('ticker_universe.csv', index_col=0, parse_dates=True)

def get_user_tickers():
    tickers_input = input("Enter ticker symbols (comma-separated): ")
    print("\n")
    tickers_input = tickers_input.upper()
    tickers_input = [ticker.strip() for ticker in tickers_input.split(",")]
    return tickers_input

def filter_tickers(full_df, user_tickers):
    available_tickers = [ticker for ticker in user_tickers if ticker in full_df.columns]
    missing_tickers = [ticker for ticker in user_tickers if ticker not in full_df.columns]

    if missing_tickers:
        print(f"⚠️ Warning: These tickers are not in the dataset and will be skipped: {missing_tickers}")

    filtered_df = full_df[available_tickers]
    return filtered_df

def import_riskfree_rate():
    riskfree_rate_df = yf.download('^IRX', period='1mo') # 13 week treasury bills, annualised
    riskfree_rate_df = riskfree_rate_df['Close'] # We only want the closing rates
    riskfree_rate = riskfree_rate_df.iloc[-1].item() # Latest risk free rate (at the end of the dataset, -1)
    riskfree_rate = riskfree_rate/(12*100)
    return riskfree_rate