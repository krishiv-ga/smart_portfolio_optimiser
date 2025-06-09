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

# Depreciated since we use CSVs now
# def download_tickers(user_tickers):
#     today = datetime.today() # Current Date
#     today = today.replace(day=1)
#     ten_years_ago = today.replace(year=today.year - 10) # Same date but 10 years ago
#     end_date = today.strftime('%Y-%m-%d') # Yfinance requires string format
#     start_date = ten_years_ago.strftime('%Y-%m-%d')

#     raw_data = yf.download(tickers=user_tickers, start=start_date, end=end_date, interval="1mo", group_by="ticker", auto_adjust=False)
#     # adj_close_data = raw_data.xs('Adj Close', axis=1, level=1)
    
    return raw_data # change back to adjusted close data

def import_riskfree_rate():
    riskfree_rate_df = yf.download('^IRX', period='1mo') # 13 week treasury bills, annualised
    riskfree_rate_df = riskfree_rate_df['Close'] # We only want the closing rates
    riskfree_rate = riskfree_rate_df.iloc[-1].item() # Latest risk free rate (at the end of the dataset, -1)
    riskfree_rate = riskfree_rate/(12*100)
    return riskfree_rate