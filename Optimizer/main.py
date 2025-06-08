# Imports
from dataloader import import_riskfree_rate, import_ticker
from metrics import get_percent_returns, get_expected_return
if __name__ == "__main__":
    print("Works!") #run code here
    ticker_df = import_ticker()
    riskfree_rate = import_riskfree_rate()
    percent_returns_df = get_percent_returns(ticker_df)
    expected_return = get_expected_return(percent_returns_df)