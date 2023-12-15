import numpy as np

# Define the corner points and their corresponding active constraint matrices
corners = {
    (0, 0): [[-1, 0],
             [0, -1]],
    (30, 0): [[4, 6],
              [0, -1]],
    (24, 4): [[4, 6],
              [2, 6]],
    (6, 10): [[2, 6],
              [0, 1]],
    (0, 10): [[1, 0],
              [0, -1]]
}

# Objective function coefficient
c = np.array([2, 4])

# Iterate over each corner point and solve the system AT y = c
for corner, matrix in corners.items():
    AT = np.transpose(matrix)
    y_values = np.linalg.solve(AT, c)

    print(f"For corner point {corner}, y-values are: {y_values}")

    # Check if y-values are non-negative
    if (y_values >= 0).all():
        print(f"Corner point {corner} has non-negative y-values and could be an optimal solution!")