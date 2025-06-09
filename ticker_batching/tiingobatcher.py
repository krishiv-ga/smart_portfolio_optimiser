from tiingo import TiingoClient
import pandas as pd
import time
import os

# Set API key
os.environ["TIINGO_API_KEY"] = "48b11fd860504fe755757ee724cfcbd1d149fd83"

# Configure
config = {
    'session': True,
    'api_key': os.getenv("TIINGO_API_KEY")
}
client = TiingoClient(config)

# Your ticker list5
tickers = ['PSA', 'WELL','AVB', 'VTR', 'O', 'NEE', 'DUK', 'SO', 'AEP', 'EXC', 'D', 'SRE', 'ETR', 'XEL', 'ES']

# Time range
start_date = "2019-06-01"
end_date = "2024-06-01"

# Output directory
output_folder = "tiingo_batches"
os.makedirs(output_folder, exist_ok=True)

# Batch and download
batch_size = 10
for i in range(0, len(tickers), batch_size):
    batch = tickers[i:i+batch_size]
    print(f"Fetching: {batch}")
    for ticker in batch:
        try:
            df = client.get_dataframe(ticker,
                                      frequency='monthly',
                                      startDate=start_date,
                                      endDate=end_date)
            df = df[['adjClose']].round(2)
            df.to_csv(f"{output_folder}/{ticker}.csv")
        except Exception as e:
            print(f"Failed to fetch {ticker}: {e}")
        time.sleep(1.2)  # ~83 requests/min safety margin (Tiingo = 100/min max)
    print(f"Batch {i//batch_size + 1} complete.\n---")
    time.sleep(3)  # optional pause between batches