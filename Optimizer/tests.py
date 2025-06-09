from dataloader import *
tickers = get_user_tickers()
tickers_df = download_tickers(tickers)

print(tickers_df.columns)
