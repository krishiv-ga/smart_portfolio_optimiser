# Imports
from dataloader import import_riskfree_rate, import_ticker, get_user_tickers, download_tickers
from metrics import get_percent_returns, get_expected_return, get_volatility, get_covariance, get_number_of_assets
from optimizer import create_initial_weights, negative_sharpe_ratio, minimize_negative_sharpe_ratio

# Main
if __name__ == "__main__":
    # ticker_df = import_ticker() # Obtain our ticker data
    user_tickers = get_user_tickers()

    ticker_df = download_tickers(user_tickers)

    riskfree_rate = import_riskfree_rate() # Obtain our risk free rate 

    percent_returns_df = get_percent_returns(ticker_df) # Need to use percent returns to show change

    expected_returns_series = get_expected_return(percent_returns_df) # Expected returns needed for pretty much all the math

    volatility_series = get_volatility(percent_returns_df, expected_returns_series) # Volatility of each ticker

    covariance_df = get_covariance(percent_returns_df) # Covariance of each ticker with each other

    number_of_assets =  get_number_of_assets(ticker_df.columns) # Need to select the number of tickers we are considering

    initial_weights = create_initial_weights(number_of_assets) # Blank array for optimizer to fill

    # DO NOT calculate sharpe_ratio beforehand
    # Instead, pass the function itself
    optimal_weights, max_sharpe = minimize_negative_sharpe_ratio(
        number_of_assets, negative_sharpe_ratio, initial_weights, expected_returns_series, covariance_df, riskfree_rate)

    # Test Output section
    print("\n")
    print("Tickers (df)")
    print(ticker_df.head)
    print("\n")
    print("Percent Returns (df)")
    print(percent_returns_df)
    print("\n")
    print("Covariance (df)")
    print(covariance_df)
    print("\n")
    print("Expected Returns (series)")
    print(expected_returns_series)
    print("\n")
    print("Volatility (series)")
    print(volatility_series)
    print("\n")
    print("Risk free rate: " + str(riskfree_rate*100) + "%")
    print("\n")
    print("Number of assets: " + str(number_of_assets))
    print("\n")
    print("Optimal Weights")
    for ticker, weight in zip(expected_returns_series.index, optimal_weights):
        print(f"{ticker}: {weight:.4f}")
    print("\n")
    print("Max Sharpe Ratio: " + str(max_sharpe))