import pandas as pd

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
