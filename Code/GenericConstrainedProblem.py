import cvxpy as cp
import numpy

# A generic constrained material problem:
products = ["Ale","Beer"]
ingredients = ["Corn","Hops","Malt"]
profit = [13,23]
recipe = [[5,4,35],[15,4,20]]
limits = [480,160,1190]

x = cp.Variable(len(products))
objective = cp.Maximize(cp.sum([profit[i] * x[i] for i in range(len(products))]))
constraints = [cp.sum([recipe[i][j]*x[i] for i in range(len(products))])<= limits[j] for j in range(len(ingredients))]

prob = cp.Problem(objective,constraints)

result = prob.solve()
[print(products[i],":",x[i].value) for i in range(len(products))]
print("Profit:",result)