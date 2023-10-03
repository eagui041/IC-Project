import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import calmap

# Function definition: Consider adding a comment explaining the function's purpose and parameters.
def append_weather_data(csv_directory="./weather_data"):
# Assignment: Consider adding a comment explaining the variable's purpose.
    dfs = []
# Loop: Consider adding a comment explaining what the loop does.
    for filename in os.listdir(csv_directory):
# Conditional statement: Consider adding a comment explaining the condition's purpose.
        if filename.startswith("en_climate_daily_ON_6105976_") and filename.endswith("_P1D.csv"):
# Assignment: Consider adding a comment explaining the variable's purpose.
            filepath = os.path.join(csv_directory, filename)
# Assignment: Consider adding a comment explaining the variable's purpose.
            df = pd.read_csv(filepath)
            dfs.append(df)
# Assignment: Consider adding a comment explaining the variable's purpose.
    final_df = pd.concat(dfs, ignore_index=True)
# Assignment: Consider adding a comment explaining the variable's purpose.
    relevant_columns = ['Min Temp (°C)', 'Max Temp (°C)', 'Total Precip (mm)', 'Year', 'Month', 'Day']
# Assignment: Consider adding a comment explaining the variable's purpose.
    final_df = final_df[relevant_columns]
# Assignment: Consider adding a comment explaining the variable's purpose.
    column_mapping = {
        'Min Temp (°C)': 'Min_Temp',
        'Max Temp (°C)': 'Max_Temp',
        'Total Precip (mm)': 'Total_Precip',
        'Year': 'Year',
        'Month': 'Month',
        'Day': 'Day'
    }
# Assignment: Consider adding a comment explaining the variable's purpose.
    final_df.rename(columns=column_mapping, inplace=True)
    return final_df

# Function definition: Consider adding a comment explaining the function's purpose and parameters.
def filter_weather_data(df, product_req_file='product_req.csv'):
# Assignment: Consider adding a comment explaining the variable's purpose.
    product_req_df = pd.read_csv(product_req_file)
# Assignment: Consider adding a comment explaining the variable's purpose.
    noras_zero = 0
# Assignment: Consider adding a comment explaining the variable's purpose.
    min_temp_condition = product_req_df['Min_Temp'][noras_zero]
# Assignment: Consider adding a comment explaining the variable's purpose.
    max_temp_condition = product_req_df['Max_Temp'][noras_zero]
# Assignment: Consider adding a comment explaining the variable's purpose.
    total_precip_condition = product_req_df['Total_Precip'][noras_zero]
# Assignment: Consider adding a comment explaining the variable's purpose.
    filtered_df = df[
# Assignment: Consider adding a comment explaining the variable's purpose.
        (df['Min_Temp'] >= min_temp_condition) & 
# Assignment: Consider adding a comment explaining the variable's purpose.
        (df['Max_Temp'] <= max_temp_condition) & 
# Assignment: Consider adding a comment explaining the variable's purpose.
        (df['Total_Precip'] <= total_precip_condition)
    ]
    return filtered_df

# Function definition: Consider adding a comment explaining the function's purpose and parameters.
def visual_option1(df):
    """
    Creates a bar graph visualization based on the input DataFrame.
    Shows the average count of days per month that meet the criteria.
    """
    # It's often a good practice to work on a copy of the DataFrame to avoid unintentional modifications
# Assignment: Consider adding a comment explaining the variable's purpose.
    df = df.copy()
    
    # Use the .loc[] accessor to avoid the SettingWithCopyWarning
# Assignment: Consider adding a comment explaining the variable's purpose.
    condition = (df['Min_Temp'] > 10) & (df['Max_Temp'] < 38) & (df['Total_Precip'] == 0)
# Assignment: Consider adding a comment explaining the variable's purpose.
    df.loc[:, 'Counts'] = np.where(condition, 1, 0)
    
# Assignment: Consider adding a comment explaining the variable's purpose.
    month_counts = df.groupby('Month').sum()['Counts']
    
# Assignment: Consider adding a comment explaining the variable's purpose.
    months = list(range(1, 13))
# Assignment: Consider adding a comment explaining the variable's purpose.
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
# Loop: Consider adding a comment explaining what the loop does.
    average_counts = {month: 0 for month in months}
    
# Loop: Consider adding a comment explaining what the loop does.
    for month, count in month_counts.items():
# Assignment: Consider adding a comment explaining the variable's purpose.
        average_counts[month] = count / len(df['Year'].unique())
    
# Assignment: Consider adding a comment explaining the variable's purpose.
    plt.bar(months, average_counts.values(), align='center', tick_label=month_names)
    plt.xlabel('Month')
    plt.title('Average Days per Month')
    plt.show()

# Function definition: Consider adding a comment explaining the function's purpose and parameters.
def visual_option2(df):
    """
    Creates a calendar heatmap visualization based on the input DataFrame.
# Loop: Consider adding a comment explaining what the loop does.
    Shows the count of days that meet the criteria for each month-day combination.
    """
    # It's often a good practice to work on a copy of the DataFrame to avoid unintentional modifications
# Assignment: Consider adding a comment explaining the variable's purpose.
    df = df.copy()
    
    # Use the .loc[] accessor to avoid the SettingWithCopyWarning
# Assignment: Consider adding a comment explaining the variable's purpose.
    df.loc[:, 'Datetime'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
# Assignment: Consider adding a comment explaining the variable's purpose.
    df.set_index('Datetime', inplace=True)
    
    # Filter rows based on the criteria and create a 'Counts' column
# Assignment: Consider adding a comment explaining the variable's purpose.
    condition = (df['Min_Temp'] > 10) & (df['Max_Temp'] < 38) & (df['Total_Precip'] == 0)
# Assignment: Consider adding a comment explaining the variable's purpose.
    df.loc[:, 'Counts'] = np.where(condition, 1, 0)
    
    # Group the data by "Month:Day" pairs and sum the 'Counts'
# Assignment: Consider adding a comment explaining the variable's purpose.
    grouped_counts_by_day = df.groupby([df.index.month, df.index.day]).sum()['Counts']
    
    # New DataFrame for the grouped data
# Assignment: Consider adding a comment explaining the variable's purpose.
    new_grouped_df = pd.DataFrame({
        'Month': grouped_counts_by_day.index.get_level_values(0),
        'Day': grouped_counts_by_day.index.get_level_values(1),
        'Counts': grouped_counts_by_day.values
    })
    
    # Adding a synthetic year to the new DataFrame
# Assignment: Consider adding a comment explaining the variable's purpose.
    synthetic_year = 2000
# Assignment: Consider adding a comment explaining the variable's purpose.
    new_grouped_df['Year'] = synthetic_year
    
    # Creating a DatetimeIndex using the synthetic year
# Assignment: Consider adding a comment explaining the variable's purpose.
    new_grouped_df['Datetime'] = pd.to_datetime(new_grouped_df[['Year', 'Month', 'Day']])
    
    # Setting the new 'Datetime' column as the index
# Assignment: Consider adding a comment explaining the variable's purpose.
    new_grouped_df.set_index('Datetime', inplace=True)
    
    # Visualize the data using calmap
# Assignment: Consider adding a comment explaining the variable's purpose.
    plt.figure(figsize=(20, 10))
# Assignment: Consider adding a comment explaining the variable's purpose.
    calmap.yearplot(new_grouped_df['Counts'], cmap='YlGn', fillcolor='#f5f5f5', daylabels=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], dayticks=[0, 1, 2, 3, 4, 5, 6], monthticks=[5], linewidth=2)
    plt.show()

# Function definition: Consider adding a comment explaining the function's purpose and parameters.
def main():
# Assignment: Consider adding a comment explaining the variable's purpose.
    appended_data = append_weather_data()
# Assignment: Consider adding a comment explaining the variable's purpose.
    filtered_data = filter_weather_data(appended_data)
    print("Select a visualization option:")
    print("1. Bar Graph (Average Days per Month)")
    print("2. Calendar Heatmap (Counts by Day of Year)")
# Assignment: Consider adding a comment explaining the variable's purpose.
    choice = input("Enter your choice (1/2): ")
# Conditional statement: Consider adding a comment explaining the condition's purpose.
    if choice == "1":
        visual_option1(filtered_data)
        print("Complete!")
# Conditional statement: Consider adding a comment explaining the condition's purpose.
    elif choice == "2":
        visual_option2(filtered_data)
        print("Complete!")
# Conditional statement: Consider adding a comment explaining the condition's purpose.
    else:
        print("Invalid choice. Please select either 1 or 2.")

# Conditional statement: Consider adding a comment explaining the condition's purpose.
if __name__ == "__main__":
    main()
