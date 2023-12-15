import cvxpy as cp
import numpy as np

# Set up the two indices we're with
Months = ["First","Second","Third","Fourth"]
Cans = ["Large","Small"]

# decision variables
Produced = cp.Variable((len(Months),len(Cans)),pos = True) # P(i,j) = # of cans of type j produced in month i
Stored = cp.Variable((len(Months),len(Cans)), pos = True)  # S(i,j) = # of cans of type j stored at the end of month i

# data table
Demand = [[3000,2500],
          [4500,4000],
          [3000,4000],
          [4000,4000]] # how many cans of each type we need each month
StorageSpace = [6,3] # amount of each type of can we can store
CostMake = [15,10] # how much each costs to make
CostStore = [2,1] # how much each costs to store
PlasticUsed = [5,3] # how much plastic is needed
MachineUsed = [.1,.08] # how much machine time is needed
PaintUsed = [.05,.04] # how much paint is needed


# initial condition - what is stored at the start!
# at the end of month 0, we have as many cans as we have in storage + what we produced - what we sold
constraints = [Stored[0,0] == 75 + Produced[0,0] - Demand[0][0],
              Stored[0,1] == 50 + Produced[0,1] - Demand[0][1]]

# same thing for the other three months
for i in range(len(Months) - 1):
    constraints += [Stored[i+1,0] == Stored[i,0] + Produced[i+1,0] - Demand[i+1][0]]
    constraints += [Stored[i+1,1] == Stored[i,1] + Produced[i+1,1] - Demand[i+1][1]]

# loop through the months for more constraints!
for i in range(len(Months)):
    constraints += [cp.sum([Stored[i,j]*StorageSpace[j] for j in range(len(Cans))]) <= 10000]  # every month we can't use more storage space than we have
    constraints += [cp.sum([Produced[i,j]*PlasticUsed[j] for j in range(len(Cans))]) <= 30000] # can't use more plastic than I have each month
    constraints += [cp.sum([Produced[i,j]*MachineUsed[j] for j in range(len(Cans))]) <= 650]   # can't use more machine time than I have each month
    constraints += [cp.sum([Produced[i,j]*PaintUsed[j] for j in range(len(Cans))]) <= 350]     # can't use more paint than I have each month


objective = cp.Minimize(cp.sum([cp.sum([Produced[i,j]*CostMake[j]+Stored[i,j]*CostStore[j]
                    for i in range(len(Months))]) for j in range(len(Cans))])) # minimize the $ spent on storing and producing cans over the 4 month period


prob = cp.Problem(objective,constraints)

result = prob.solve()

print("Total Cost:",result)
print("\n\nNumber Produced:\n",Produced.value)
print("\n\nNumber Stored:\n",Stored.value)