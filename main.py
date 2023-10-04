import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import calmap

# Function to append all the CSV files in the directory
def append_weather_data(csv_directory="./weather_data"):
    dfs = []
    for filename in os.listdir(csv_directory):
        if filename.startswith("en_climate_daily_ON_6105976_") and filename.endswith("_P1D.csv"):
            filepath = os.path.join(csv_directory, filename)
            df = pd.read_csv(filepath)
            dfs.append(df)
    final_df = pd.concat(dfs, ignore_index=True)
    relevant_columns = ['Min Temp (°C)', 'Max Temp (°C)', 'Total Precip (mm)', 'Year', 'Month', 'Day']
    final_df = final_df[relevant_columns]
    column_mapping = {
        'Min Temp (°C)': 'Min_Temp',
        'Max Temp (°C)': 'Max_Temp',
        'Total Precip (mm)': 'Total_Precip',
        'Year': 'Year',
        'Month': 'Month',
        'Day': 'Day'
    }
    final_df.rename(columns=column_mapping, inplace=True)
    return final_df

# Function to filter the appended DataFrame
def filter_weather_data(df, product_req_file='product_req.csv'):
    product_req_df = pd.read_csv(product_req_file)
    noras_zero = 0
    min_temp_condition = product_req_df['Min_Temp'][noras_zero]
    max_temp_condition = product_req_df['Max_Temp'][noras_zero]
    total_precip_condition = product_req_df['Total_Precip'][noras_zero]
    filtered_df = df[
        (df['Min_Temp'] >= min_temp_condition) & 
        (df['Max_Temp'] <= max_temp_condition) & 
        (df['Total_Precip'] <= total_precip_condition)
    ]
    return filtered_df

# Function to create a bar graph visualization
def visual_option1(df):
    """
    Creates a bar graph visualization based on the input DataFrame.
    Shows the average count of days per month that meet the criteria.
    """
    # Copy the DataFrame to avoid unintentional modifications
    df = df.copy()
    
    # Use the .loc[] accessor to avoid the SettingWithCopyWarning
    condition = (df['Min_Temp'] > 10) & (df['Max_Temp'] < 38) & (df['Total_Precip'] == 0)
    df.loc[:, 'Counts'] = np.where(condition, 1, 0)
    
    month_counts = df.groupby('Month').sum()['Counts']
    
    months = list(range(1, 13))
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    average_counts = {month: 0 for month in months}
    
    for month, count in month_counts.items():
        average_counts[month] = count / len(df['Year'].unique())
    
    plt.bar(months, average_counts.values(), align='center', tick_label=month_names)
    plt.xlabel('Month')
    plt.title('Average Days per Month')
    plt.show()

# Function to create a calendar heatmap visualization
def visual_option2(df):
    """
    Creates a calendar heatmap visualization based on the input DataFrame.
    Shows the count of days that meet the criteria for each month-day combination.
    """
    # Copy the DataFrame to avoid unintentional modifications
    df = df.copy()
    
    # Use the .loc[] accessor to avoid the SettingWithCopyWarning
    df.loc[:, 'Datetime'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
    df.set_index('Datetime', inplace=True)
    
    # Filter rows based on the criteria and create a 'Counts' column
    condition = (df['Min_Temp'] > 10) & (df['Max_Temp'] < 38) & (df['Total_Precip'] == 0)
    df.loc[:, 'Counts'] = np.where(condition, 1, 0)
    
    # Group the data by "Month:Day" pairs and sum the 'Counts'
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
    
    # Visualize the data using calmap
    plt.figure(figsize=(20, 10))
    calmap.yearplot(new_grouped_df['Counts'], cmap='YlGn', fillcolor='#f5f5f5', daylabels=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], dayticks=[0, 1, 2, 3, 4, 5, 6], monthticks=[5], linewidth=2)
    plt.show()

# Main function
def main():
    appended_data = append_weather_data()
    filtered_data = filter_weather_data(appended_data)
    print("Select a visualization option:")
    print("1. Bar Graph (Average Days per Month)")
    print("2. Calendar Heatmap (Counts by Day of Year)")
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        visual_option1(filtered_data)
        print("Complete!")
    elif choice == "2":
        visual_option2(filtered_data)
        print("Complete!")
    else:
        print("Invalid choice. Please select either 1 or 2.")

# Call the main function
if __name__ == "__main__":
    main()
