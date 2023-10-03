import pandas as pd
import numpy as np
import calmap
import matplotlib.pyplot as plt

# Sample dataset (replace with your own data)
data = pd.read_csv('train.csv', parse_dates=['date_time'])
data['year'] = data.date_time.dt.year

# Filter data for the year 2010 and select relevant columns
data_2010 = data[data['year'] == 2010]
data_2010 = data_2010[['date_time', 'deg_C']]

# Set the date_time column as the index
data_2010.set_index('date_time', inplace=True)

# Create the calendar heatmap using calmap
plt.figure(figsize=(20, 10))
calmap.yearplot(data_2010['deg_C'], cmap='YlGn', fillcolor='lightgrey', daylabels='MTWTFSS', dayticks=[0, 2, 4, 6], linewidth=2)

# Customize the appearance (optional)
plt.title('Calendar Heatmap for Temperature in 2010')
plt.xlabel('Months')
plt.ylabel('Days of the Week')

# Show the calendar heatmap
plt.show()
