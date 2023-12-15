import cvxpy as cp

# set up our table
Metals = ["Alloy 1","Alloy 2","Alloy 3","Scrap 1","Scrap 2"]
cost = [150,120,80,35,20]
availability = [50,50,20,30,40]
carbon = [1.75,2.45,2.8,3.1,3.5]
nickel = [2,3,4,4.5,5.5]
chromium = [3.5,.8,1.2,3.9,2.8]
strength = [60000,40000,90000,120000,70000]

# define decision variable
x = cp.Variable(len(Metals))

# define total cost
totalCost = cp.sum([cost[i]*x[i] for i in range(len(Metals))])


# define total for each component
totalCarbon = cp.sum([carbon[i]*x[i] for i in range(len(Metals))])
totalNickel = cp.sum([nickel[i]*x[i] for i in range(len(Metals))])
totalChromium = cp.sum([chromium[i]*x[i] for i in range(len(Metals))])
totalStrength = cp.sum([strength[i]*x[i] for i in range(len(Metals))])

# define total mass of metal
total = cp.sum([x[i] for i in range(len(Metals))])

# objective
objective = cp.Minimize(totalCost)

# define constraints
constraints = [total == 100, # total mass is 100
               totalStrength <= 80000*total,
               totalStrength >= 50000*total,
               totalCarbon >= total*2,
               totalCarbon <= total*3,
               totalNickel <= total*4,
               totalChromium >= total*1.3,
               totalChromium <= total*2.7
]

# use append and either a list or a loop to add the availability constraints
for i in range(len(Metals)):
    constraints.append(x[i] <= availability[i])


prob = cp.Problem(objective, constraints)

result = prob.solve()

[print(Metals[i], ":", x[i].value) for i in range(len(Metals))]
print("Cost:", result)