import numpy as np

# Create a matrix
A = np.array([[1, 2], [3, 4]])

# Compute the inverse of the matrix
A_inv = np.linalg.inv(A)

print("Inverse of Matrix A:")
print(A_inv)




# The inverse of a matrix is another matrix that, when multiplied by the original matrix, 
# results in the identity matrix.