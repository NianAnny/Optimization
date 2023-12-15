import cvxpy as cp
import numpy as np

# Define the problem data
P = np.array([[13, 12, -2],
              [12, 17, 6],
              [-2, 6, 12]])
q = np.array([-22.0, -14.5, 13.0])
r = 1.0

# variable
x = cp.Variable(3)

# objective
objective = cp.Minimize((1/2)*cp.quad_form(x, P) + q.T @ x + r)

# Define the constraints
constraints = [-1 <= x, x <= 1]

problem = cp.Problem(objective, constraints)
problem.solve()
print("The optimal value of x is:", x.value)
