import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset into a pandas DataFrame
data = pd.read_csv('filtered_weather_data.csv')

# Create a new column 'Month_Year' that combines 'Year' and 'Month'
data['Month_Year'] = data['Year'].astype(str) + '-' + data['Month'].astype(str).str.zfill(2)

# Group the data by 'Month_Year' and count the number of unique 'Day' values
monthly_counts = data.groupby('Month_Year')['Day'].nunique()

# Calculate the average number of days per month
average_days_per_month = monthly_counts.mean()

# Create a bar graph to visualize the data without a y-axis
plt.figure(figsize=(10, 5))
plt.bar(monthly_counts.index, monthly_counts.values)
plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('')
plt.title(f'Average Days per Month: {average_days_per_month:.2f}')
plt.tight_layout()
plt.show()
