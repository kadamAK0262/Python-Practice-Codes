# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, 
# or a table with rows and columns.
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df) 

#refer to the row index:
print(df.loc[0])

# Indexing 
df1 = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df1) 