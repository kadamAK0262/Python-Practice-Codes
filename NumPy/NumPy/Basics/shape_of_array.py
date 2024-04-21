import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

arr1 = np.array([1, 2, 3, 4], ndmin=5)  # Create an array with 5 dimensions using ndmin

print(arr1)
print('shape of array :', arr1.shape)