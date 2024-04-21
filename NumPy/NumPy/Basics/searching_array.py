import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)
print(x)
print("Index of value 4:", x[0])


# Search for values greater than 3
greater_than_3 = arr[arr > 3]
print("Values greater than 3:", greater_than_3)


arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.where(arr1%2 == 1)  # searching odd numbers
print(y)