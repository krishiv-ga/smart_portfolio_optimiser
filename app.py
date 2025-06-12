# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from dataloader import import_riskfree_rate, import_ticker, filter_tickers
from metrics import get_percent_returns, get_expected_return, get_volatility, get_covariance, get_number_of_assets
from optimizer import create_initial_weights, entropy, minimize_negative_sharpe_ratio_with_entropy

# Setup
st.set_page_config(page_title="Smart Portfolio Optimizer", layout="wide")
st.title("📊 Smart Portfolio Optimizer")

# Step 1: Load full ticker data
ticker_full_df = import_ticker()  # This must include 'Symbol' and 'Name' columns

# Prepare ticker-name map
ticker_names = {
    row['Symbol']: f"{row['Symbol']} - {row['Name']}" for _, row in ticker_full_df.iterrows()
}

# Step 2: Multiselect UI
selected_symbols = st.multiselect(
    "Select Stocks for Portfolio Optimization:",
    options=list(ticker_names.keys()),
    format_func=lambda x: ticker_names[x],
    default=["AAPL", "MSFT", "AMZN"]  # Set some good defaults
)

if selected_symbols:
    if st.button("Optimize Portfolio"):
        try:
            # Step 3: Run optimizer
            ticker_df = filter_tickers(ticker_full_df, selected_symbols)
            riskfree_rate = import_riskfree_rate()

            percent_returns_df = get_percent_returns(ticker_df)
            expected_returns_series = get_expected_return(percent_returns_df)
            volatility_series = get_volatility(percent_returns_df, expected_returns_series)
            covariance_df = get_covariance(percent_returns_df)

            number_of_assets = get_number_of_assets(ticker_df.columns)
            initial_weights = create_initial_weights(number_of_assets)
            entropy_weight = entropy(initial_weights)

            optimal_weights, max_sharpe = minimize_negative_sharpe_ratio_with_entropy(
                number_of_assets,
                initial_weights,
                expected_returns_series.values,
                covariance_df,
                riskfree_rate,
                entropy_weight=0.05
            )

            # Step 4: Output
            st.subheader("📈 Optimized Portfolio Results")
            st.write(f"**Risk-Free Rate:** {riskfree_rate*100:.2f}%")
            st.write(f"**Max Sharpe Ratio:** {max_sharpe:.4f}")

            full_names = [ticker_names[symbol] for symbol in expected_returns_series.index]
            results_df = pd.DataFrame({
                "Stock": full_names,
                "Symbol": expected_returns_series.index,
                "Optimal Weight": optimal_weights,
                "Expected Return": expected_returns_series.values,
                "Volatility": volatility_series.values
            })

            st.dataframe(results_df.style.format({
                "Optimal Weight": "{:.4f}",
                "Expected Return": "{:.2%}",
                "Volatility": "{:.2%}"
            }))

            # Pie Chart
            fig, ax = plt.subplots()
            ax.pie(optimal_weights, labels=full_names, autopct="%1.1f%%", startangle=90)
            ax.axis("equal")
            st.pyplot(fig)

        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")
else:
    st.info("Please select at least one stock to begin.")
