import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Importing Ticker data
# Sample test until proper yf ticker filtering is implemented
def import_ticker():
    return pd.read_csv('Optimizer/ticker_data.csv', index_col=0)

# def get_user_tickers():
#     tickers_input = input("Enter ticker symbols (comma-separated): ")
#     tickers_input = tickers_input.upper()
#     tickers_input.strip()
#     tickers_input = tickers_input.split(",")
#     return tickers_input


# def download_tickers(user_tickers):
#     today = datetime.today() # Current Date
#     today = today.replace(day=1)
#     ten_years_ago = today.replace(year=today.year - 10) # Same date but 10 years ago
#     end_date = today.strftime('%Y-%m-%d') # Yfinance requires string format
#     start_date = ten_years_ago.strftime('%Y-%m-%d')

#     raw_data = yf.download(tickers=user_tickers, start=start_date, end=end_date, interval="1mo", group_by="ticker", auto_adjust=False)
#     # adj_close_data = raw_data.xs('Adj Close', axis=1, level=1)
    
#     return raw_data # change back to adjusted close data

def import_riskfree_rate():
    riskfree_rate_df = yf.download('^IRX', period='1mo') # 13 week treasury bills, annualised
    riskfree_rate_df = riskfree_rate_df['Close'] # We only want the closing rates
    riskfree_rate = riskfree_rate_df.iloc[-1].item() # Latest risk free rate (at the end of the dataset, -1)
    riskfree_rate = riskfree_rate/(12*100)
    return riskfree_rate