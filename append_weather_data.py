import os
import pandas as pd

# Directory where all the CSV files are located
csv_directory = "./weather_data"

# List to hold DataFrame objects
dfs = []

# Loop through each CSV file in the directory
for filename in os.listdir(csv_directory):
    if filename.startswith("en_climate_daily_ON_6105976_") and filename.endswith("_P1D.csv"):
        filepath = os.path.join(csv_directory, filename)
        
        # Read each CSV file into a DataFrame
        df = pd.read_csv(filepath)
        
        # Append the DataFrame to the list
        dfs.append(df)

# Concatenate all DataFrames in the list
final_df = pd.concat(dfs, ignore_index=True)

# Keep only relevant columns
relevant_columns = [
    'Min Temp (°C)',
    'Max Temp (°C)',
    'Total Precip (mm)',
    'Year',
    'Month',
    'Day'
]
final_df = final_df[relevant_columns]

# Rename the columns
column_mapping = {
    'Min Temp (°C)': 'Min_Temp',
    'Max Temp (°C)': 'Max_Temp',
    'Total Precip (mm)': 'Total_Precip',
    'Year': 'Year',
    'Month': 'Month',
    'Day': 'Day'
}
final_df.rename(columns=column_mapping, inplace=True)

# Save the concatenated DataFrame to a new CSV file
final_df.to_csv("appended_weather_data.csv", index=False)
