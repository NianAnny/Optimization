import cvxpy as cp
import numpy as np

def f(x, y):
    return (x - 2)**2 + (y - 1)**4

# Gradient of the function
def grad_f(x, y):
    df_dx = 2 * (x - 2)
    df_dy = 4 * (y - 1)**3
    return np.array([df_dx, df_dy])

# Initial guess
x, y = 0, 0
print(f"Initial guess: {(x,y)}; Gradient: {grad_f(x, y)}")

# positive t (step size)
t = cp.Variable()

grad = grad_f(x, y)
# "-" sign for negative gradient
new_x = 0 + t * -grad[0]
new_y = 0 + t * -grad[1]

# Define the objective function f at the new point
new_f = f(new_x, new_y)

problem = cp.Problem(cp.Minimize(new_f))
result = problem.solve()
print(f"\n(a) step size = {t.value}; optimal = {result}")
print(f"new point (x, y) = {(new_x.value, new_y.value)}")

# Backtracking line search parameters
alpha, beta, t = 0.1, 0.5, 1

# Backtracking line search algorithm
while True:
    x_new, y_new = x + t * -grad[0], y + t * -grad[1]

    if f(x_new, y_new) <= f(x, y) - alpha * t * np.dot(grad.T, grad):
        break
    else:
        t = beta * t
print(f"\n(b) step size = {t}; new point (x, y) = {x_new, y_new}")