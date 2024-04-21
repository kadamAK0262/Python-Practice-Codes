import numpy as np

# Creating matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
product = np.dot(A, B)

# Transpose of a matrix
transpose_A = np.transpose(A)

# Determinant of a matrix
det_A = np.linalg.det(A)

print("Matrix Multiplication:")
print(product)
print("Transpose of Matrix A:")
print(transpose_A)
print("Determinant of Matrix A:")
print(det_A)
