import pandas as pd
import matplotlib.pyplot as plt

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
