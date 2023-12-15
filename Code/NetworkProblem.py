import cvxpy as cp

# we'll use i = {0,1,2} for plants and j = {0,1,2,3} for cities
plants = ["A", "B", "C", "D"]
cities = ["1", "2", "3", "4"]
supply = [85, 115, 100, 100000]
demand = [115, 70, 65, 75]
cost = [[10, 7, 10, 6],
        [7, 12, 16, 9],
        [12, 8, 13, 7],
        [50, 40, 60, 75]]

# decision variable
x = cp.Variable((len(supply), len(demand)), pos=True)

totalCost = cp.sum([cp.sum([cost[i][j] * x[i][j] for j in range(len(cities))]) for i in range(len(plants))])
objective = cp.Minimize(totalCost)

constraints = []

# supply constraints
for i in range(len(plants)):
    constraints += [cp.sum([x[i][j] for j in range(len(cities))]) <= supply[i]]

# demand constraints
for j in range(len(cities)):
    constraints += [cp.sum([x[i][j] for i in range(len(plants))]) >= demand[j]]

prob = cp.Problem(objective, constraints)

result = prob.solve()

[[print(plants[i], "->", cities[j], x[i][j].value) for j in range(len(cities))] for i in range(len(plants))]
print("Cost:", result)
########################################################################################################
print(" ")
import cvxpy as cp
import numpy as np

A = [[0, 9, 0, 8, 0, 0],
     [0, 0, 5, 0, 7, 0],
     [0, 0, 0, 0, 0, 10],
     [0, 0, 10, 0, 7, 0],
     [0, 0, 0, 0, 0, 12],
     [0, 0, 0, 0, 0, 0]]

x = cp.Variable((6, 6), pos=True)

constraints = []

for i in range(len(A)):
    for j in range(len(A[0])):
        constraints += [x[i, j] <= A[i][j]]

for i in range(1, len(A) - 1):
    constraints += [cp.sum([x[i, j] for j in range(len(A))]) <= cp.sum([x[j, i] for j in range(len(A))])]

objective = cp.Maximize(cp.sum([x[i, 5] for i in range(len(A))]))

prob = cp.Problem(objective, constraints)

result = prob.solve()
[[print(j, "->", i, ":", x[j][i].value) for i in range(len(A))] for j in range(len(A))]
print("Total Delivered:", result)
########################################################################################################
print(" ")
supply = [100000, 0, 0, 0, 0, 0]
maxOut = [sum(row) for row in A]
maxOut[5] = 10000

# loop through cities. In this loop j is the source city and i is the destination
for j in [0, 1, 3, 2, 4]:
    for i in [1, 3, 2, 4, 5]:
        send = min([A[j][i], supply[j],
                    maxOut[i] - supply[i]])  # send the max along an arc you can until you run out of supply

        # subtract sent amount from source city and add it to destination city
        supply[j] = supply[j] - send
        supply[i] = supply[i] + send

    print(supply)