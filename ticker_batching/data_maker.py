import yfinance as yf
import pandas as pd

# Define tickers and date range
tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOGL"]
start_date = "2014-06-01"
end_date = "2024-06-01"

# Download all data (multi-index columns)
raw_data = yf.download(tickers, start=start_date, end=end_date, interval="1mo", group_by="ticker", auto_adjust=False)

# Extract the 'Adj Close' layer from the second level (Price Type)
adj_close_data = raw_data.xs('Adj Close', axis=1, level=1)


# Extract only 'Adj Close' from the multi-indexed DataFrame
data = adj_close_data

# Clean and export
data = data.dropna().round(2)
data.to_csv("ticker_data.csv")

print("✅ CSV saved: ticker_data")
print(data.head())
