# import pandas as pd

# def get_data():

#     file_paths = [
#         "graph data/Brent Oil Futures Historical Data.csv",
#         "graph data/Copper Futures Historical Data.csv",
#         "graph data/Gold Futures Historical Data.csv",
#         "graph data/Natural Gas Futures Historical Data.csv",
#         "graph data/Platinum Futures Historical Data.csv",
#         "graph data/Silver Futures Historical Data.csv",
#     ]


#     columns_to_drop = ["Change %"]

#     for file_path in file_paths:

#         df = pd.read_csv(file_path)
#         df = df.drop(columns_to_drop, axis=1)
        
#     return df
# get_data()
import pandas as pd

def get_data():

    file_paths = [
        "graph data/Brent Oil Futures Historical Data.csv",
        "graph data/Copper Futures Historical Data.csv",
        "graph data/Gold Futures Historical Data.csv",
        "graph data/Natural Gas Futures Historical Data.csv",
        "graph data/Platinum Futures Historical Data.csv",
        "graph data/Silver Futures Historical Data.csv",
    ]

    columns_to_drop = ["Change %"]
    dfs = []  # List to store DataFrames from each file

    for file_path in file_paths:
        df = pd.read_csv(file_path)
        df = df.drop(columns_to_drop, axis=1)
        dfs.append(df)  # Append the current DataFrame to the list

    # Concatenate all DataFrames in the list into a single DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)
        
    return combined_df

data = get_data()
print(data)
