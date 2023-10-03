import pandas as pd
import numpy as np
import calmap
import matplotlib.pyplot as plt

file_path = "appended_weather_data.csv"

# Read the dataset into a pandas DataFrame
df = pd.read_csv(file_path)

# Step 1: Combine the Year, Month, and Day columns to create a new column with datetime values.
# Use pandas' to_datetime function to combine the Year, Month, and Day columns into a datetime format
df['Datetime'] = pd.to_datetime(df[['Year', 'Month', 'Day']])

# Step 2: Set the new 'Datetime' column as a DatetimeIndex for the DataFrame
df.set_index('Datetime', inplace=True)

# Adjusting the Counts column based on the conditions
df['Counts'] = np.where((df['Min_Temp'] > 10) & (df['Max_Temp'] < 38) & (df['Total_Precip'] == 0), 1, 0)

# Resample the data on a daily frequency and sum the counts
daily_counts = df.resample('D').sum()['Counts']


plt.figure(figsize=(20, 10))
# Set the fillcolor to your desired color for null/zero values, for example, off-white
calmap.yearplot(daily_counts, cmap='YlGn', fillcolor='#f5f5f5', daylabels=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], dayticks=[0, 1, 2, 3, 4, 5, 6],monthticks=[3], linewidth=2)
plt.show()
#result plot_test_6.txt