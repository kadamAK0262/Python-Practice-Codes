import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

arr1 = arr.reshape(4, 3)
print(arr1)

arr2 = arr.reshape(2, 3, 2)
print(arr2)