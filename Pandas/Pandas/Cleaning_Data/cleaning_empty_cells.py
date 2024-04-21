import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()
print(new_df.to_string())

df.dropna(inplace = True)       # Remove all rows with NULL values
print(df.to_string())

# Replace NULL values with the number 130.
df.fillna(130, inplace = True)

# Replace Only For Specified Columns.
df["Calories"].fillna(130, inplace = True)  # Replace NULL values in the "Calories" columns with the number 130.