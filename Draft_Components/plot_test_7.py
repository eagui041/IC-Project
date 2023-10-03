import pandas as pd
import numpy as np
import calmap
import matplotlib.pyplot as plt

# Step 1: Load the data
file_path = "appended_weather_data.csv"
df = pd.read_csv(file_path)

# Step 2: Combine the Year, Month, and Day columns to create a datetime index
df['Datetime'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
df.set_index('Datetime', inplace=True)

# Step 3: Filter rows based on the criteria and create a 'Counts' column
df['Counts'] = np.where((df['Min_Temp'] > 10) & (df['Max_Temp'] < 38) & (df['Total_Precip'] == 0), 1, 0)

# Step 4: Group the data by "Month:Day" pairs and sum the 'Counts'
grouped_counts_by_day = df.groupby([df.index.month, df.index.day]).sum()['Counts']

# Creating a completely new DataFrame for the grouped data
new_grouped_df = pd.DataFrame({
    'Month': grouped_counts_by_day.index.get_level_values(0),
    'Day': grouped_counts_by_day.index.get_level_values(1),
    'Counts': grouped_counts_by_day.values
})

# Adding a synthetic year (e.g., 2000) to the new DataFrame
synthetic_year = 2000
new_grouped_df['Year'] = synthetic_year

# Creating a DatetimeIndex using the synthetic year
new_grouped_df['Datetime'] = pd.to_datetime(new_grouped_df[['Year', 'Month', 'Day']])

# Setting the new 'Datetime' column as the index
new_grouped_df.set_index('Datetime', inplace=True)

# Step 5: (Optional) Visualize the data
plt.figure(figsize=(20, 10))
calmap.yearplot(new_grouped_df['Counts'], cmap='YlGn', fillcolor='#f5f5f5', daylabels=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], dayticks=[0, 1, 2, 3, 4, 5, 6], monthticks=[3], linewidth=2)
plt.show()
