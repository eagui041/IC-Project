import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import calmap

# Define a function
def append_weather_data(csv_directory="./weather_data"):
# Assign value to variable
    dfs = []
# Iterate through elements
    for filename in os.listdir(csv_directory):
# Check conditions
        if filename.startswith("en_climate_daily_ON_6105976_") and filename.endswith("_P1D.csv"):
# Assign value to variable
            filepath = os.path.join(csv_directory, filename)
# Assign value to variable
            df = pd.read_csv(filepath)
            dfs.append(df)
# Assign value to variable
    final_df = pd.concat(dfs, ignore_index=True)
# Assign value to variable
    relevant_columns = ['Min Temp (°C)', 'Max Temp (°C)', 'Total Precip (mm)', 'Year', 'Month', 'Day']
# Assign value to variable
    final_df = final_df[relevant_columns]
# Assign value to variable
    column_mapping = {
        'Min Temp (°C)': 'Min_Temp',
        'Max Temp (°C)': 'Max_Temp',
        'Total Precip (mm)': 'Total_Precip',
        'Year': 'Year',
        'Month': 'Month',
        'Day': 'Day'
    }
# Assign value to variable
    final_df.rename(columns=column_mapping, inplace=True)
    return final_df

# Define a function
def filter_weather_data(df, product_req_file='product_req.csv'):
# Assign value to variable
    product_req_df = pd.read_csv(product_req_file)
# Assign value to variable
    noras_zero = 0
# Assign value to variable
    min_temp_condition = product_req_df['Min_Temp'][noras_zero]
# Assign value to variable
    max_temp_condition = product_req_df['Max_Temp'][noras_zero]
# Assign value to variable
    total_precip_condition = product_req_df['Total_Precip'][noras_zero]
# Assign value to variable
    filtered_df = df[
# Assign value to variable
        (df['Min_Temp'] >= min_temp_condition) & 
# Assign value to variable
        (df['Max_Temp'] <= max_temp_condition) & 
# Assign value to variable
        (df['Total_Precip'] <= total_precip_condition)
    ]
    return filtered_df

# Define a function
def visual_option1(df):
    """
    Creates a bar graph visualization based on the input DataFrame.
    Shows the average count of days per month that meet the criteria.
    """
    # It's often a good practice to work on a copy of the DataFrame to avoid unintentional modifications
# Assign value to variable
    df = df.copy()
    
    # Use the .loc[] accessor to avoid the SettingWithCopyWarning
# Assign value to variable
    condition = (df['Min_Temp'] > 10) & (df['Max_Temp'] < 38) & (df['Total_Precip'] == 0)
# Assign value to variable
    df.loc[:, 'Counts'] = np.where(condition, 1, 0)
    
# Assign value to variable
    month_counts = df.groupby('Month').sum()['Counts']
    
# Assign value to variable
    months = list(range(1, 13))
# Assign value to variable
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
# Iterate through elements
    average_counts = {month: 0 for month in months}
    
# Iterate through elements
    for month, count in month_counts.items():
# Assign value to variable
        average_counts[month] = count / len(df['Year'].unique())
    
# Assign value to variable
    plt.bar(months, average_counts.values(), align='center', tick_label=month_names)
    plt.xlabel('Month')
    plt.title('Average Days per Month')
    plt.show()

# Define a function
def visual_option2(df):
    """
    Creates a calendar heatmap visualization based on the input DataFrame.
# Iterate through elements
    Shows the count of days that meet the criteria for each month-day combination.
    """
    # It's often a good practice to work on a copy of the DataFrame to avoid unintentional modifications
# Assign value to variable
    df = df.copy()
    
    # Use the .loc[] accessor to avoid the SettingWithCopyWarning
# Assign value to variable
    df.loc[:, 'Datetime'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
# Assign value to variable
    df.set_index('Datetime', inplace=True)
    
    # Filter rows based on the criteria and create a 'Counts' column
# Assign value to variable
    condition = (df['Min_Temp'] > 10) & (df['Max_Temp'] < 38) & (df['Total_Precip'] == 0)
# Assign value to variable
    df.loc[:, 'Counts'] = np.where(condition, 1, 0)
    
    # Group the data by "Month:Day" pairs and sum the 'Counts'
# Assign value to variable
    grouped_counts_by_day = df.groupby([df.index.month, df.index.day]).sum()['Counts']
    
    # New DataFrame for the grouped data
# Assign value to variable
    new_grouped_df = pd.DataFrame({
        'Month': grouped_counts_by_day.index.get_level_values(0),
        'Day': grouped_counts_by_day.index.get_level_values(1),
        'Counts': grouped_counts_by_day.values
    })
    
    # Adding a synthetic year to the new DataFrame
# Assign value to variable
    synthetic_year = 2000
# Assign value to variable
    new_grouped_df['Year'] = synthetic_year
    
    # Creating a DatetimeIndex using the synthetic year
# Assign value to variable
    new_grouped_df['Datetime'] = pd.to_datetime(new_grouped_df[['Year', 'Month', 'Day']])
    
    # Setting the new 'Datetime' column as the index
# Assign value to variable
    new_grouped_df.set_index('Datetime', inplace=True)
    
    # Visualize the data using calmap
# Assign value to variable
    plt.figure(figsize=(20, 10))
# Assign value to variable
    calmap.yearplot(new_grouped_df['Counts'], cmap='YlGn', fillcolor='#f5f5f5', daylabels=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], dayticks=[0, 1, 2, 3, 4, 5, 6], monthticks=[5], linewidth=2)
    plt.show()

# Define a function
def main():
# Assign value to variable
    appended_data = append_weather_data()
# Assign value to variable
    filtered_data = filter_weather_data(appended_data)
    print("Select a visualization option:")
    print("1. Bar Graph (Average Days per Month)")
    print("2. Calendar Heatmap (Counts by Day of Year)")
# Assign value to variable
    choice = input("Enter your choice (1/2): ")
# Check conditions
    if choice == "1":
        visual_option1(filtered_data)
        print("Complete!")
# Check conditions
    elif choice == "2":
        visual_option2(filtered_data)
        print("Complete!")
# Check conditions
    else:
        print("Invalid choice. Please select either 1 or 2.")

# Check conditions
if __name__ == "__main__":
    main()
