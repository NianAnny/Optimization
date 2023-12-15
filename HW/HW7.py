import cvxpy as cp
import numpy as np
print("Problem 1:")
print("(a)")
M = cp.Variable(nonneg=True)
B = cp.Variable(nonneg=True)
constraints1a = [6 * M + 2 * B >= 6, # Protein
                5 * M + 15 * B >= 15, # Carbs
                M + B >= 2, # Vitamins
                0.6 * M + B <= 3, # Sugar
                ]
obj1 = cp.Minimize(0.3 * M + 0.2 * B)
prob1 = cp.Problem(obj1, constraints1a)
prob1.solve()
print(f"The optimal cost is ${prob1.value:0.2f}")
print(f"Optimal servings of milk is {M.value:0.1f} grams.")
print(f"Optimal serving of bread is {B.value:0.1f} grams.")

print("\n(b)")
print("(i) Remove the protein constraint")
M = cp.Variable(nonneg=True)
B = cp.Variable(nonneg=True)
constraints1 = [
                5 * M + 15 * B >= 15, # Carbs
                M + B >= 2, # Vitamins
                0.6 * M + B <= 3, # Sugar
                ]
obj1 = cp.Minimize(0.3 * M + 0.2 * B)
prob1 = cp.Problem(obj1, constraints1)
prob1.solve()
print(f"The optimal cost is ${prob1.value:0.2f}")
print(f"Optimal servings of milk is {M.value:0.1f} grams.")

print(f"Optimal serving of bread is {B.value:0.1f} grams.")

print("\n(ii) Remove the vitamin constraint")
M = cp.Variable(nonneg=True)
B = cp.Variable(nonneg=True)
constraints1 = [6 * M + 2 * B >= 6, # Protein
                5 * M + 15 * B >= 15, # Carbs

                0.6 * M + B <= 3, # Sugar
                ]
obj1 = cp.Minimize(0.3 * M + 0.2 * B)
prob1 = cp.Problem(obj1, constraints1)
prob1.solve()
print(f"The optimal cost is ${prob1.value:0.2f}")
print(f"Optimal servings of milk is {M.value:0.1f} grams.")
print(f"Optimal serving of bread is {B.value:0.1f} grams.")

print("\n(iii) Remove the sugar constraint")
M = cp.Variable(nonneg=True)
B = cp.Variable(nonneg=True)
constraints1 = [6 * M + 2 * B >= 6, # Protein
                5 * M + 15 * B >= 15, # Carbs
                M + B >= 2 # Vitamins

                ]
obj1 = cp.Minimize(0.3 * M + 0.2 * B)
prob1 = cp.Problem(obj1, constraints1)
prob1.solve()
print(f"The optimal cost is ${prob1.value:0.2f}")
print(f"Optimal servings of milk is {M.value:0.1f} grams.")
print(f"Optimal serving of bread is {B.value:0.1f} grams.")

print("\n(iv) Add sodium constraint")
M = cp.Variable(nonneg=True)
B = cp.Variable(nonneg=True)
constraints1 = [6 * M + 2 * B >= 6, # Protein
                5 * M + 15 * B >= 15, # Carbs
                M + B >= 2, # Vitamins
                0.6 * M + B <= 3, # Sugar
                12 * B + 5 * M <= 30 # Sodium
                ]
obj1 = cp.Minimize(0.3 * M + 0.2 * B)
prob1 = cp.Problem(obj1, constraints1)
prob1.solve()
print(f"The optimal cost is ${prob1.value:0.2f}")
print(f"Optimal servings of milk is {M.value:0.1f} grams.")
print(f"Optimal serving of bread is {B.value:0.1f} grams.")

print("\n(e)")
print("Shadow Price for Protein: ", constraints1a[0].dual_value)
print("Shadow Price for Carbs: ", constraints1a[1].dual_value)
print("Shadow Price for Vitamins: ", constraints1a[2].dual_value)
print("Shadow Price for Sodium: ", constraints1a[3].dual_value)

#########################################################################
print("\nProblem 2:")
print("(a)")
DVD = ["Q75-1", "Q100-5"]
Q = cp.Variable(len(DVD), nonneg=True)
con2 = [2*Q[0] + 3*Q[1] <= 385,
        Q[0] + 2*Q[1] <=240,
        5*Q[0] + 4*Q[1] <=700]
prob2 = cp.Problem(cp.Maximize(55*Q[0]+75*Q[1]), con2)
prob2.solve()
print(f"Optimal Profit is ${prob2.value:.0f} with {Q[0].value:.0f} {DVD[0]} players and {Q[1].value:.0f} {DVD[1]} players.")

print(f"\n(b) Shadow Price for Production: {con2[0].dual_value}")

print(f"\n(c) Shadow Price for Testing: {con2[2].dual_value}")

print("\n(e)")
DVD = ["Q75-1", "Q100-5"]
Q = cp.Variable(len(DVD), nonneg=True)
con2 = [2*Q[0] + 3*Q[1] <= 385,
        Q[0] + 2*Q[1] <=240,
        5*Q[0] + 4*Q[1] <=700,
        Q[1] - Q[0] >=10]
prob2 = cp.Problem(cp.Maximize(55*Q[0]+75*Q[1]), con2)
prob2.solve()
print(f"Optimal Profit is ${prob2.value:.0f} with {Q[0].value:.0f} {DVD[0]} players and {Q[1].value:.0f} {DVD[1]} players.")
for i in range(len(con2)):
    print(con2[i].dual_value)

#############################################################################
print("\nProblem 3:")
print("(a)")
S = cp.Variable(nonneg=True)
H = cp.Variable(nonneg=True)
M = cp.Variable(nonneg=True)
OT1 = cp.Variable(nonneg=True) # Overtime hours on machine 1
OT2 = cp.Variable(nonneg=True) # Overtime hours on machine 2

cost_hours = 30*(3*S + 7*H + 9*M) + 40*(4*S + 5*H + 7*M)
cost_overtime = 65*OT1 + 90*OT2
objective = cp.Minimize(cost_hours + cost_overtime)
cons3 = [540*S + 760*H + 950*M >= 45000,
         3*S + 7*H + 9*M <= 350 + OT1,
         4*S + 5*H + 7*M <= 300 + OT2,
         S >= 25,
         H >= 25,
         M >= 10
]
prob = cp.Problem(objective, cons3)
prob.solve()
print(f"Minimum cost: ${prob.value}")
print(f"Standard doors: {S.value}")
print(f"High Security doors: {H.value}")
print(f"Maximum Security doors: {M.value}")
print(f"Overtime hours on machine 1: {OT1.value}")
print(f"Overtime hours on machine 2: {OT2.value}")

print("\n(b)")
cost_hours = (30+10)*(3*S + 7*H + 9*M) + 40*(4*S + 5*H + 7*M)
cost_overtime = 65*OT1 + 90*OT2
objectiveb = cp.Minimize(cost_hours + cost_overtime)
cons3b = [540*S + 760*H + 950*M >= 45000,
         3*S + 7*H + 9*M <= 350 + OT1,
         4*S + 5*H + 7*M <= 300 + OT2,
         S >= 25,
         H >= 25,
         M >= 10
]
prob = cp.Problem(objectiveb, cons3b)
prob.solve()
print(f"Minimum cost: ${prob.value}")
print(f"Standard doors: {S.value}")
print(f"High Security doors: {H.value}")
print(f"Maximum Security doors: {M.value}")
print(f"Overtime hours on machine 1: {OT1.value}")
print(f"Overtime hours on machine 2: {OT2.value}")

print("\n(c) Shadow Price for Maximum Security doors:", cons3[5].dual_value) # Original Problem

print("\n(d) Shadow Price for Management Revenue:", cons3[0].dual_value)
cost_hours = 30*(3*S + 7*H + 9*M) + 40*(4*S + 5*H + 7*M)
cost_overtime = 65*OT1 + 90*OT2
objectivec = cp.Minimize(cost_hours + cost_overtime)
cons3d = [540*S + 760*H + 950*M >= 50000,
         3*S + 7*H + 9*M <= 350 + OT1,
         4*S + 5*H + 7*M <= 300 + OT2,
         S >= 25,
         H >= 25,
         M >= 10
]
prob = cp.Problem(objectivec, cons3d)
prob.solve()
print(f"Minimum cost: ${prob.value}")
print(f"Standard doors: {S.value}")
print(f"High Security doors: {H.value}")
print(f"Maximum Security doors: {M.value}")
print(f"Overtime hours on machine 1: {OT1.value}")
print(f"Overtime hours on machine 2: {OT2.value}")

###############################################################
print("\nProblem 4:")
Month = ["1", "2", "3"]
engines = ["Truck", "Car"]
Produced = cp.Variable((len(Month),len(engines)), nonneg = True) # P(i,j) = number of engine j produced in month i
Stored = cp.Variable((len(Month),len(engines)), nonneg = True)  # S(i,j) = number of engine j stored at the end of month i
demand = [[400, 800],
          [300, 500],
          [500, 600]] # demand for each month
cost = [2000, 1500]
labor = [10, 8]
holding_cost = [150, 150]
max_labor_hours = 9000
combined_production = 1000
initial_storage = [100, 200]
end_storage = [100, 100]

# At the end of the first month, we have initial storage + what we produced - what was demanded
constraints4 = [Stored[0, 0] == initial_storage[0] + Produced[0, 0] - demand[0][0], # Truck
                Stored[0, 1] == initial_storage[1] + Produced[0, 1] - demand[0][1]] # Car

# Constraints for storage and production in subsequent months
# same thing for the other months
for i in range(len(Month)-1):
    constraints4.append(Stored[i+1,0] == Stored[i,0] + Produced[i+1,0] - demand[i+1][0])
    constraints4.append(Stored[i+1,1] == Stored[i,1] + Produced[i+1,1] - demand[i+1][1])

# end of the third month constraint
for j in range(len(engines)):
    constraints4.append(Stored[2,j] >= end_storage[j])

# each month constraints
for i in range(len(Month)):
    constraints4.append(cp.sum([Produced[i,j] for j in range(len(engines))]) <= combined_production)
    constraints4.append(cp.sum([Produced[i,j]*labor[j] for j in range(len(engines))]) <= max_labor_hours)

objective4 = cp.Minimize(cp.sum([cp.sum([Produced[i,j]*cost[j] + Stored[i,j]*holding_cost[j]
                                for i in range(len(Month))]) for j in range(len(engines))]))

prob4 = cp.Problem(objective4, constraints4)
result4 = prob4.solve()

# Output the results
print(f"Total Cost: ${result4}")
print("Number Produced each month (Trucks, Cars):\n", Produced.value)
print("Number Stored at the end of each month (Trucks, Cars):\n", Stored.value)

print("\n(a)")
for i in range(len(constraints4)):
    print(constraints4[i])
print("\nShadow Prices for labor constraints")
print(constraints4[9].dual_value)
print(constraints4[11].dual_value)
print(constraints4[13].dual_value)

print("\n(b)")
print("Shadow Prices for production constraints")
print(constraints4[8].dual_value)
print(constraints4[10].dual_value)
print(constraints4[12].dual_value)
# At the end of the first month, we have initial storage + what we produced - what was demanded
constraints4b = [Stored[0, 0] == initial_storage[0] + Produced[0, 0] - demand[0][0], # Truck
                Stored[0, 1] == initial_storage[1] + Produced[0, 1] - demand[0][1]] # Car

# Constraints for storage and production in subsequent months
# same thing for the other months
for i in range(len(Month)-1):
    constraints4b.append(Stored[i+1,0] == Stored[i,0] + Produced[i+1,0] - demand[i+1][0])
    constraints4b.append(Stored[i+1,1] == Stored[i,1] + Produced[i+1,1] - demand[i+1][1])
for j in range(len(engines)):
    constraints4b.append(Stored[2,j] >= end_storage[j])

for i in range(len(Month)):
    constraints4b.append(cp.sum([Produced[i,j]*labor[j] for j in range(len(engines))]) <= max_labor_hours)

for i in range(len(Month)-1):
    constraints4b.append(cp.sum([Produced[i,j] for j in range(len(engines))]) <= combined_production)

constraints4b.append(Produced[2,0] + Produced[2,1] <= combined_production+10)


objective4b = cp.Minimize(cp.sum([cp.sum([Produced[i,j]*cost[j] + Stored[i,j]*holding_cost[j]
                                for i in range(len(Month))]) for j in range(len(engines))]))

prob4b = cp.Problem(objective4b, constraints4b)
result4b = prob4b.solve()

# Output the results
print(f"\nTotal Cost: ${result4b}")
print("Number Produced each month (Trucks, Cars):\n", Produced.value)
print("Number Stored at the end of each month (Trucks, Cars):\n", Stored.value)
print(f"min cost change: {result4-result4b}")

print("\n(c)")
demandc1 = [[400, 800],
          [300, 500],
          [500, 550]] # demand for each month
# At the end of the first month, we have initial storage + what we produced - what was demanded
constraints4c1 = [Stored[0, 0] == initial_storage[0] + Produced[0, 0] - demandc1[0][0], # Truck
                Stored[0, 1] == initial_storage[1] + Produced[0, 1] - demandc1[0][1]] # Car
for i in range(len(Month)-1):
    constraints4c1.append(Stored[i+1,0] == Stored[i,0] + Produced[i+1,0] - demandc1[i+1][0])
    constraints4c1.append(Stored[i+1,1] == Stored[i,1] + Produced[i+1,1] - demandc1[i+1][1])
for j in range(len(engines)):
    constraints4c1.append(Stored[2,j] >= end_storage[j])
for i in range(len(Month)):
    constraints4c1.append(cp.sum([Produced[i,j] for j in range(len(engines))]) <= combined_production)
    constraints4c1.append(cp.sum([Produced[i,j]*labor[j] for j in range(len(engines))]) <= max_labor_hours)
objective4c1 = cp.Minimize(cp.sum([cp.sum([Produced[i,j]*cost[j] + Stored[i,j]*holding_cost[j]
                                for i in range(len(Month))]) for j in range(len(engines))]))
prob4c1 = cp.Problem(objective4c1, constraints4c1)
result4c1 = prob4c1.solve()
print("Optimal Solution after decreasing M3 car demand to 550:")
print(f"Total Cost: ${result4c1}")
print("Number Produced each month (Trucks, Cars):\n", Produced.value)
print("Number Stored at the end of each month (Trucks, Cars):\n", Stored.value)

demandc2 = [[400, 800],
          [300, 500],
          [500, 450]] # demand for each month
# At the end of the first month, we have initial storage + what we produced - what was demanded
constraints4c2 = [Stored[0, 0] == initial_storage[0] + Produced[0, 0] - demandc2[0][0], # Truck
                Stored[0, 1] == initial_storage[1] + Produced[0, 1] - demandc2[0][1]] # Car
for i in range(len(Month)-1):
    constraints4c2.append(Stored[i+1,0] == Stored[i,0] + Produced[i+1,0] - demandc2[i+1][0])
    constraints4c2.append(Stored[i+1,1] == Stored[i,1] + Produced[i+1,1] - demandc2[i+1][1])
for j in range(len(engines)):
    constraints4c2.append(Stored[2,j] >= end_storage[j])
for i in range(len(Month)):
    constraints4c2.append(cp.sum([Produced[i,j] for j in range(len(engines))]) <= combined_production)
    constraints4c2.append(cp.sum([Produced[i,j]*labor[j] for j in range(len(engines))]) <= max_labor_hours)
objective4c2 = cp.Minimize(cp.sum([cp.sum([Produced[i,j]*cost[j] + Stored[i,j]*holding_cost[j]
                                for i in range(len(Month))]) for j in range(len(engines))]))
prob4c2 = cp.Problem(objective4c2, constraints4c2)
result4c2 = prob4c2.solve()
print("\nOptimal Solution after decreasing M3 car demand to 450:")
print(f"Total Cost: ${result4c2}")
print("Number Produced each month (Trucks, Cars):\n", Produced.value)
print("Number Stored at the end of each month (Trucks, Cars):\n", Stored.value)

##############################################################
print("\nProblem 5:")
Plant = ["Plant 1", "Plant 2", "Plant 3"]
City = ["City 1", "City 2", "City 3", "City 4"]
costs = np.array([[8, 6, 10, 9],
                [9, 12, 13, 7],
                [14, 9, 16, 5]])
Supply = [35, 50, 40]
Demand = [45, 20, 30, 30]
x = cp.Variable((len(Plant), len(City)), nonneg=True)
obj5 = cp.Minimize(cp.sum(cp.multiply(costs, x)))
constraints5 = []
for i in range(len(Plant)):
    constraints5.append(cp.sum(x[i, :]) <= Supply[i])
for j in range(len(City)):
    constraints5.append(cp.sum(x[:, j]) == Demand[j])
prob5 = cp.Problem(obj5, constraints5)
prob5.solve()
print(f"Optimal Cost: ${prob5.value:.2f}")
print("Electricity Distribution (million kwh):")
print(x.value)
for i in range(len(Plant)):
    for j in range(len(City)):
        print(f"{Plant[i]} -> {City[j]}: {x.value[i,j]:.2f}")

print("\nShadow Prices")
for i in range(len(constraints5)):
    print(constraints5[i])
    print(constraints5[i].dual_value)






