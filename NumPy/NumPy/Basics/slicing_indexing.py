import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Accessing individual elements
print("Element at (0, 0):", arr[0, 0])
print("Element at (1, 2):", arr[1, 2])

# Slicing rows and columns
print("First row:", arr[0, :])
print("Second column:", arr[:, 1])
print("Subarray from (0, 1) to (1, 2):")
print(arr[0:2, 1:3])