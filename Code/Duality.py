import cvxpy as cp
import numpy as np

x = cp.Variable(2, pos = True)

objective = cp.Maximize(2*x[0]+4*x[1])

constraints = [4*x[0]+6*x[1] <= 120,
               2*x[0]+6*x[1] <= 72,
                 x[1] <= 10]

prob = cp.Problem(objective, constraints)

result = prob.solve()


print(result)
print(x.value)

y = cp.Variable(3, pos = True)

objective = cp.Minimize(120*y[0] + 72*y[1] + 10*y[2])

constraints = [4*y[0]+2*y[1] >= 2,
              6*y[0]+6*y[1]+y[2] >= 4]

prob = cp.Problem(objective,constraints)

result = prob.solve()
print(result)
print(y.value)