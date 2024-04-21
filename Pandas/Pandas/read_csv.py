import pandas as pd

df = pd.read_csv('customer.csv')
print(df.to_string())   # use to_string() to print the entire DataFrame.

print(pd.options.display.max_rows)   # number of maximum returned rows.

# pd.options.display.max_rows = 9999   # Increase the maximum number of rows to display the entire DataFrame