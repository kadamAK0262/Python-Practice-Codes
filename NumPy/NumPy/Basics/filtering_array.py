import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4, 5])

filter_even = arr % 2 == 0

even_numbers = arr[filter_even]
print("Even numbers:", even_numbers)
