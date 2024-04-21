# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

print(myvar[0])    # for return first value

# Indexing with labels :    With the index argument, you can name your own labels.
myvar1 = pd.Series(a, index = ["x", "y", "z"])
print(myvar1)



#  Key Value Object series.
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar2 = pd.Series(calories)

myvar3 = pd.Series(calories, index = ["day1", "day2"]) #Indexing 

print(myvar2)
print(myvar3)