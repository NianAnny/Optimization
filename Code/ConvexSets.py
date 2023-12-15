import numpy as np

# Set up the coefficient matrix A and vector b for the system Ax = b
A = np.array([
    [0, 10, 24, 30, 0],  # Equation 1 coefficients
    [10, 6, 4, 0, 0],   # Equation 2 coefficients
    [1, 1, 1, 1, 1]     # Equation 3 coefficients
])

b = np.array([3, 4, 1])  # Right-hand side of equations

# Solve for x using least squares method
x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

for i in range(len(x)):
    print(f'x{i} = {x[i]}')
print(sum(x))