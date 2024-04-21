# Replace Using Mean, Median, or Mode.

# Mean = the average value (the sum of all values divided by number of values).
import pandas as pd

df = pd.read_csv('data.csv')

x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)
print(df.to_string())

# Median = the value in the middle, after you have sorted all values ascending.

y = df["Calories"].median()
df["Calories"].fillna(y, inplace = True)


# Mode = the value that appears most frequently.

z = df["Calories"].mode()[0]
df["Calories"].fillna(z, inplace = True)