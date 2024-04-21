# Singular Value Decomposition (SVD):
# decomposes a matrix into three separate matrices: U, S, and V. U contains left singular vectors, 
# S is a diagonal matrix containing singular values, and V is the transpose of right singular vectors.

import numpy as np

# Create a matrix
A = np.array([[1, 2], [3, 4], [5, 6]])

# Perform singular value decomposition
U, S, V = np.linalg.svd(A)

print("U matrix:")
print(U)
print("Singular values:")
print(S)
print("V transpose matrix:")
print(V)
