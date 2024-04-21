import pandas as pd

df = pd.read_csv('customer.csv')

# Display the first few rows of the DataFrame.
print(df.head())
# print(df.head(10))  # Display the first 10 rows of the DataFrame.

# # Display the last few rows of the DataFrame
print(df.tail())

# Display summary statistics of the DataFrame
print(df.describe())

# Display information about the DataFrame (columns, data types, memory usage)
print(df.info())