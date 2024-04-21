import numpy as np

arr = np.array([3, 1, 4, 2, 5])

# Sort the array in ascending order
sorted_arr = np.sort(arr)
print("Sorted array (ascending):", sorted_arr)

# Sort the array in descending order
reverse_sorted_arr = np.sort(arr)[::-1]
print("Sorted array (descending):", reverse_sorted_arr)

# string array
strarr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(strarr))