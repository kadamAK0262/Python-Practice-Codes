import numpy as np

# Generate a 1D array of 5 random integers between 0 and 9
random_array = np.random.randint(10, size=5)
print("Random Array:", random_array)


arr = np.arange(10)

# Shuffle the array
np.random.shuffle(arr)   # shuffles the elements of an array in-place
print("Shuffled Array:", arr)