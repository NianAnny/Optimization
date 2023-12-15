import numpy as np

# Given data
A = np.array([[1, 1, 1, 0],
              [1, -1, 0, 1]])
c = np.array([5, 1, 0, 0])
b = np.array([7, 3])

# Initialization
basicVars = [2, 3]
nonbasicVars = [0, 1]
B = A[:, basicVars]
N = A[:, nonbasicVars]
xB = np.array([7, 3])

# Main loop for the simplex method
while True:
    # Compute dual variables (y)
    cB = c[basicVars]
    y = np.dot(np.linalg.inv(B.T), cB)

    # Calculate reduced costs
    cN = c[nonbasicVars]
    cNbar = cN - np.dot(N.T, y)

    # Optimality check
    if np.all(cNbar <= 0):
        break

    # Determine entering variable (most positive reduced cost)
    entering_index = np.argmax(cNbar)
    entering = nonbasicVars[entering_index]

    # Compute direction dB
    dB = np.linalg.solve(B, -A[:, entering])

    # Calculate ratios to determine leaving variable and step size
    ratios = np.where(dB < 0, -b / dB, np.inf)
    step_size = np.min(ratios)
    leaving_index = np.argmin(ratios)
    leaving = basicVars[leaving_index]

    # Update solution and basis
    b = b - step_size * dB
    basicVars[leaving_index], nonbasicVars[entering_index] = entering, leaving
    B = A[:, basicVars]
    N = A[:, nonbasicVars]

    # Print the state of the algorithm
    print(f"Entering variable: x{entering}")
    print(f"Leaving variable: x{leaving}")
    print("Current Solution (xB):", b)
    print("Objective value:", np.dot(cB, b))
    print("-----")

# Print optimal solution
print("Optimal solution reached:", b)
