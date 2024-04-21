import numpy as np

# Coefficients of the linear equations
A = np.array([[2, 1], [1, -1]])
b = np.array([5, 1])

# Solve the system of linear equations
solution = np.linalg.solve(A, b)

print("Solution:")
print(solution)
