import cvxpy as cp
import numpy as np

Months = ["First","Second","Third","Fourth","Fifth","Sixth"]
Staff = cp.Variable(len(Months),integer = True)
Produced = cp.Variable(len(Months),pos = True)
Stored = cp.Variable(len(Months), pos = True)
Fired = cp.Variable(len(Months),pos = True)
Hired = cp.Variable(len(Months),pos = True)
Overtime = cp.Variable(len(Months),pos = True)

Demand = [6000,500,8000,4000,7000,5000]

constraints = [Stored[0] == 1000 + Produced[0] - Demand[0],
              Staff[0] == 15 + Hired[0] - Fired[0]]

for i in range(len(Months) - 1):
    constraints += [Stored[i+1] == Stored[i] + Produced[i+1] - Demand[i+1]]
    constraints += [Staff[i+1] == Staff[i] + Hired[i+1] - Fired[i+1]]

for i in range(len(Months)):
    constraints += [Stored[i] <= 3000]
    constraints += [Produced[i] == 600*Staff[i] + 3*Overtime[i]]
    constraints += [Overtime[i] <= 40*Staff[i]]

objective = cp.Minimize(cp.sum([5*Stored[i] + 3000*Staff[i] + 75*Overtime[i] + 2000*Hired[i] + 3000*Fired[i]
                                for i in range(len(Months))]))

prob = cp.Problem(objective,constraints)

result = prob.solve()

print("Total Cost:",result)
print("Produced:",Produced.value)
print("Sold:",Demand)
print("Stored:",Stored.value)
print("Staff:",Staff.value)
print("Hired:",Hired.value)
print("Fired:",Fired.value)
print("Overtime:",Overtime.value)





