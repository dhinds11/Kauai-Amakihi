import pandas as pd
import glob
import os

# Define the path to your CSV files (e.g., in a 'data' folder)
# Use a wildcard '*' to match all CSV files in the directory
path = '/home/dhind/Kauai-Amakihi/Annotations/macaulay/csv files/reformatted files/*.csv' 

# Get a list of all CSV file paths
all_files = glob.glob(path)

# Create an empty list to store individual DataFrames
df_list = []

# Loop through each file, read it into a DataFrame, and append to the list
for filename in all_files:
    df = pd.read_csv(filename)
    df_list.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
# ignore_index=True renumbers the rows of the combined DataFrame
combined_df = pd.concat(df_list, ignore_index=True)

savepath = '/home/dhind/Kauai-Amakihi/Annotations/macaulay/combined_output.csv'
# Optionally, save the combined DataFrame to a new CSV file
combined_df.to_csv(savepath, index=False)

print("CSV files combined successfully!")
