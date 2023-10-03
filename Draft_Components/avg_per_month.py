import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("filtered_weather_data.csv")

# Create a new column to represent the date
df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])

# Group the data by Month and Year and count the number of days in each month
monthly_counts = df.groupby(['Year', 'Month'])['Date'].count().reset_index()

# Calculate the average count of days per month across the entire dataset
average_counts = monthly_counts['Date'].mean()

# Print the result
print("Average count of days per month:", average_counts)
