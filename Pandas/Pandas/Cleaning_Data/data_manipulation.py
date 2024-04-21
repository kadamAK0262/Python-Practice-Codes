import pandas as pd

df = pd.read_csv('data.csv')

# Set "Duration" = 45 in row 7.
df.loc[7, 'Duration'] = 45


# Loop through all values in the "Duration" column.
# If the value is higher than 120, set it to 120:
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120


# Delete rows where "Duration" is higher than 120.
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)


# Sort the DataFrame by a column
df.sort_values(by='Duration', ascending=False, inplace=True)


# Returns True for every row that is a duplicate, otherwise False:
print(df.duplicated())

# Remove all duplicates.
df.drop_duplicates(inplace = True)


# Group data by a column and calculate summary statistics
grouped = df.groupby('Duration').mean()
print(grouped)