import numpy as np
from scipy.optimize import fsolve

# given fuction
def f(x, y):
    return (x - 2)**2 + (y - 1)**4

# Gradient of the function
def grad_f(x, y):
    df_dx = 2 * (x - 2)
    df_dy = 4 * (y - 1)**3
    return np.array([df_dx, df_dy])

# Initialization
x0 = [0, 0]
tolerance = 10**(-5)
alpha = 0.3
beta = 0.7

def exact_line_search(grad_f, x0, tolerance):
    def grad_objective(alpha, x0, descent_dir):
        return np.dot(grad_f(*(x0 + alpha * descent_dir)).T, descent_dir)
    x = x0
    descent_dir = -grad_f(*x)
    while np.linalg.norm(descent_dir) > tolerance:
        alpha_star = fsolve(grad_objective, 0, args=(x, descent_dir))
        x = x + alpha_star * descent_dir
        descent_dir = -grad_f(*x)
    return x


def backtracking_line_search(grad_f, x0, tolerance, alpha, beta):
    x = x0
    descent_dir = -grad_f(*x)
    while np.linalg.norm(descent_dir) > tolerance:
        t = 1
        while f(*x) + alpha * t * np.dot(grad_f(*x).T, descent_dir) < f(*(x + t * descent_dir)):
            t = beta * t
        x = x + t * descent_dir
        descent_dir = -grad_f(*x)
    return x

optimal_exact = exact_line_search(grad_f, x0, tolerance)
optimal_backtracking = backtracking_line_search(grad_f, x0, tolerance, alpha, beta)
print(f"A. {optimal_exact}")
print(f"B. {optimal_backtracking}")
