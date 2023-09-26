import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import calmap

#Section: append_weather_data.py
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

#Section: filter_weather_data.py
# Read the 'appended_weather_data.csv' and 'product_req.csv' files into DataFrames
appended_weather_data_df = pd.read_csv('appended_weather_data.csv')
product_req_df = pd.read_csv('product_req.csv')

# Filtering conditions from 'product_req.csv'
noras_zero = 0
min_temp_condition = product_req_df['Min_Temp'][noras_zero]
max_temp_condition = product_req_df['Max_Temp'][noras_zero]
total_precip_condition = product_req_df['Total_Precip'][noras_zero]


# Apply the filtering conditions to 'appended_weather_data.csv'
filtered_weather_data_df = appended_weather_data_df[
    (appended_weather_data_df['Min_Temp'] >= min_temp_condition) &
    (appended_weather_data_df['Max_Temp'] <= max_temp_condition) &
    (appended_weather_data_df['Total_Precip'] == total_precip_condition)
]

# Save the filtered DataFrame to a new CSV file
filtered_weather_data_df.to_csv('filtered_weather_data.csv', index=False)

#Section: visual_option1


# Path to dataset
file_path = "filtered_weather_data.csv"

# Read the dataset into a pandas DataFrame
df = pd.read_csv(file_path)

# Group the data by month and calculate the count of occurrences for each month
month_counts = df.groupby('Month')['Day'].count()

# Create a list of months (1 to 12)
months = list(range(1, 13))

# Initialize a dictionary to store the average count of days per month
average_counts = {month: 0 for month in months}

# Calculate the average count of days for each month
for month, count in month_counts.items():
    average_counts[month] = count / len(df['Year'].unique())  # Divide by the number of unique years

# Create a bar graph to visualize the average counts
plt.bar(average_counts.keys(), average_counts.values(), align='center')
plt.xticks(months)
plt.xlabel('Month')
plt.title('Average Days per Month')
plt.show()

#Section: visual_option2.py

#Load the data
file_path = "appended_weather_data.csv"
df = pd.read_csv(file_path)

#Combine the Year, Month, and Day columns to create a datetime index
df['Datetime'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
df.set_index('Datetime', inplace=True)

#Filter rows based on the criteria and create a 'Counts' column
df['Counts'] = np.where((df['Min_Temp'] > 10) & (df['Max_Temp'] < 38) & (df['Total_Precip'] == 0), 1, 0)

#Group the data by "Month:Day" pairs and sum the 'Counts'
grouped_counts_by_day = df.groupby([df.index.month, df.index.day]).sum()['Counts']

# New DataFrame for the grouped data
new_grouped_df = pd.DataFrame({
    'Month': grouped_counts_by_day.index.get_level_values(0),
    'Day': grouped_counts_by_day.index.get_level_values(1),
    'Counts': grouped_counts_by_day.values
})

# Adding a synthetic year to the new DataFrame
synthetic_year = 2000
new_grouped_df['Year'] = synthetic_year

# Creating a DatetimeIndex using the synthetic year
new_grouped_df['Datetime'] = pd.to_datetime(new_grouped_df[['Year', 'Month', 'Day']])

# Setting the new 'Datetime' column as the index
new_grouped_df.set_index('Datetime', inplace=True)

#Visualize the data
plt.figure(figsize=(20, 10))
calmap.yearplot(new_grouped_df['Counts'], cmap='YlGn', fillcolor='#f5f5f5', daylabels=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], dayticks=[0, 1, 2, 3, 4, 5, 6], monthticks=[5], linewidth=2)
plt.show()

