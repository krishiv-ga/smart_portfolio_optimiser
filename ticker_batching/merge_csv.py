# Used to create 
import os
import pandas as pd

def combine_tiingo_csvs(folder_path='ticker_batching/cleaned_csvs'):
    combined_df = pd.DataFrame()

    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            ticker = filename.replace(".csv", "")
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path, index_col="date", parse_dates=True)
            df.rename(columns={"adjClose": ticker}, inplace=True)
            combined_df = pd.concat([combined_df, df[[ticker]]], axis=1)

    combined_df.sort_index(inplace=True)
    return combined_df

# Example usage
if __name__ == "__main__":
    df = combine_tiingo_csvs()
    df.to_csv("combined_tiingo_data.csv")
    print("✅ Combined file saved as combined_tiingo_data.csv")
    print(df.head())
