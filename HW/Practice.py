import cvxpy as cp

x = cp.Variable(nonneg=True)
y = cp.Variable()
objective = cp.Minimize(cp.multiply(x, cp.log(x)) + cp.exp(y))
constraints = [x + y <= 1,
               y >= 0]
problem = cp.Problem(objective, constraints)
problem.solve()

print(problem.value)
print(x.value, y.value)