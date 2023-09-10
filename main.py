import pandas as pd
import numpy as np

# Load the CSV data into a pandas DataFrame
df = pd.read_csv('Panamericanos_Lima.csv')

# Replace 'your_data.csv' with the actual path to your CSV file

# Summation of a specific column using NumPy
column_to_sum = 'Oro'
sum_value = df[column_to_sum].sum()
print(f'Sum of {column_to_sum}: {sum_value}')

# Number of elements
num_elements = len(df)
print(f'Number of elements: {num_elements}')

# Mean using NumPy
mean_value = np.mean(df[column_to_sum])
print(f'Mean of {column_to_sum}: {mean_value}')

# Mean rounded to 2 decimal places
mean_rounded = round(mean_value, 2)
print(f'Mean rounded to 2 decimals: {mean_rounded}')

# Median using NumPy
median_value = np.median(df[column_to_sum])
print(f'Median of {column_to_sum}: {median_value}')

# Mode
mode_value = df[column_to_sum].mode().iloc[0]
print(f'Mode of {column_to_sum}: {mode_value}')

# Percentiles using NumPy
percentiles = np.percentile(df[column_to_sum], [25, 50, 75])
print(f'25th Percentile: {percentiles[0]}')
print(f'50th Percentile (Median): {percentiles[1]}')
print(f'75th Percentile: {percentiles[2]}')

# Variance using NumPy
variance_value = np.var(df[column_to_sum])
print(f'Variance of {column_to_sum}: {variance_value}')
