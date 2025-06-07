import yfinance as yf
import pandas as pd

# Define FAANG tickers
tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOGL"]

# Define date range
start_date = "2014-06-01"
end_date = "2024-06-01"

raw_data = yf.download(tickers, start=start_date, end=end_date, interval="1mo", group_by='ticker', auto_adjust=False)

# Check if 'Adj Close' exists
if 'Adj Close' in raw_data.columns:
    data = raw_data['Adj Close']
else:
    data = raw_data  # Fallback: could be single-level DataFrame already

# Drop rows with any missing data
data = data.dropna().round(2)

# Save to CSV
data.to_csv("ticker_data.csv")
print("CSV file saved: faang_10yr_monthly.csv")
print(raw_data.columns)
print(raw_data.head())
