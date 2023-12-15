import cvxpy as cp

# Define variables
x = cp.Variable(nonneg=True)
y = cp.Variable(nonneg=True)

# Define constraints
constraints = [4*x + 6*y <= 120,
               2*x + 6*y <= 72,
               y <= 10]

objective = cp.Maximize(2*x + 4*y)
problem = cp.Problem(objective, constraints)
problem.solve()

# shadow price for the Machine 2 constraint
shadow_price = constraints[1].dual_value
print(f"a) Shadow price for Machine 2 constraint: {shadow_price}")


# Function to check if the basis has changed
def changeBasis(Delta):
    constraints[1] = 2*x + 6*y <= 72 + Delta
    problem = cp.Problem(objective, constraints)
    problem.solve()
    return constraints[1].dual_value == shadow_price # changed

# lower and upper bound for Delta
Delta = 0
change = 1
while changeBasis(Delta):
    Delta += change
upr = 72 + Delta

Delta = 0
while changeBasis(Delta):
    Delta -= change
lwr = 72 + Delta

print(f"b) Range of Delta for which the optimal basis remains unchanged: [{lwr}, {upr}].")