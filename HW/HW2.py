import cvxpy as cp

print("Problem 1")
print("(a)")
# decision variables
Milk = cp.Variable()
Bread = cp.Variable()

# constraints (linear program)
constraints1 = [6 * Milk + 2 * Bread >= 6, # Protein
                5 * Milk + 15 * Bread >= 15, # Carbs
                Milk + Bread >= 2, # Vitamins
                0.6 * Milk + Bread <= 3, # Sugar
                Milk >= 0,
                Bread >= 0]

# objective function
obj1 = cp.Minimize(0.3 * Milk + 0.2 * Bread)

# solve the problem
prob1 = cp.Problem(obj1, constraints1)
prob1.solve()

print(f"The optimal cost is ${prob1.value:0.2f}")
print(f"Optimal servings of milk is {Milk.value:0.1f} grams.")
print(f"Optimal serving of bread is {Bread.value:0.1f} grams.")


print("(b) Shows in the graph.")
import numpy as np
import matplotlib.pyplot as plt

# range of milk (x-axis) and axis
M = np.linspace(0, 5, 100)

# represent bread (y-axis) by M
B1 = (6-6*M)/2
B2 = (15-5*M)/15
B3 = 2-M
B4 = 3-0.6*M

# create the canvas
plt.figure(figsize = (10, 7))

# plot all constraint equations
plt.plot(M, B1, label=r'Protein: $6M + 2B \geq 6$')
plt.plot(M, B2, label=r'Carbs: $5M + 15B \geq 15$')
plt.plot(M, B3, label=r'Vitamins: $M + B \geq 2$')
plt.plot(M, B4, label=r'Sugar: $0.6M + B \leq 3$')

# feasible region
lwr = np.maximum(0, np.maximum(B1, np.maximum(B2,B3)))
plt.fill_between(M, B4, lwr, where=(B4>=lwr), alpha=0.5)

# graphing
plt.xlim(0,5)
plt.ylim(0,3)
plt.xlabel("Milk (grams)")
plt.ylabel("Bread (grams)")
plt.legend()
plt.show()

print("(c)")
print("Feasible solutions:")
print("1. M = 1 grams, B = 1 grams")
print("2. M = 3 grams, B = 0 grams")

print("Infeasible solutions: ")
print("1. M = 0 grams, B = 2 grams, cost = $0.4 ; violates the protein requirement")
print("2. M = 0 grams, B = 4 grams, cost = $0.8 ; violates the sugar constraint")

print("(d) Shows in the graph.")
# Objective function lines for different values of C
M = np.linspace(0, 10, 100)
C = 10 - 1.5*M  # C = 2

plt.figure(figsize=(10, 7))

# Plot the constraints
plt.plot(M, B1, label=r'$6M + 2B \geq 6$')
plt.plot(M, B2, label=r'$5M + 15B \geq 15$')
plt.plot(M, B3, label=r'$M + B \geq 2$')
plt.plot(M, B4, label=r'$0.6M + B \leq 3$')

# Plot the objective function lines
plt.plot(M, C, label=r'$0.3M + 0.2B = 2$')
lwr = np.maximum(0, np.maximum(B1, np.maximum(B2,B3)))
plt.fill_between(M, B4, lwr, where=(B4>=lwr), alpha=0.5)

# Arrow indicating decreasing objective value
plt.arrow(4, 5, -0.5, -0.7, head_width=0.1, head_length=0.2, fc='blue', ec='blue')

# Setting the limits and labels
plt.xlim((0, 10))
plt.ylim((0, 10))
plt.xlabel("Milk (grams)")
plt.ylabel("Bread (grams)")
plt.legend()
plt.show()

print("(e) From the graph, the corner solution will be at M = 0.5, B = 1.5 with the smallest cost value of $0.45."
      "This is the same result what we get from the Homework 1.")


######################################################
print(" ")
print("Problem 2: Solved in Problem 1(a)")
######################################################
print(" ")
# P3
print("Problem 3")
print("(a)-(b)")
# decision variables
S = cp.Variable(integer=True) # small
M = cp.Variable(integer=True) # medium
L = cp.Variable(integer=True) # large

# unknown materials cost variables, but know values after the subtraction of material costs: 40, 50, 70
# Labor costs
cost_s = 0.1*32 + 0.22*45 + 0.15*30
cost_m = 0.23*32 + 0.25*45 + 0.17*30
cost_l = 0.31*32 + 0.38*45 + 0.27*30

# objective function
profit = S*(40 - cost_s) + M*(50 - cost_m) + L*(75 - cost_l)
obj3 = cp.Maximize(profit)

# Constraints
constraints3 = [0.1*S + 0.23*M + 0.31*L <= 5,
                0.22*S + 0.25*M + 0.38*L <= 7,
                0.1*S + 0.23*M + 0.31*L >= 4,
                0.22*S + 0.25*M + 0.38*L + 0.15*S + 0.17*M + 0.27*L <= 15,
                0.27*L <= 2,
                S >= 2,
                M >= 3,
                L >= 1]

# Problem
prob3 = cp.Problem(obj3, constraints3)
prob3.solve()

print(f"The maximum profit is ${prob3.value: .2f}")
print(f"Number of Small Aircraft: {S.value: .0f}")
print(f"Number of Medium Aircraft: {M.value:.0f}")
print(f"Number of Large Aircraft: {L.value:.0f}")

print("(c): Definitely making sense to enforce integer constraints on the number of planes produced "
      "since we cannot produce a “decimal” aircraft. An aircraft is supposed to be discrete product.")

######################################################
print(" ")
# P4
print("Problem 4")
print("(b)-(c)")
# Setup table
time_collectors = [2, 2, 2, 2, 2, 2, 8, 8, 8, 8, 4, 4, 3, 3, 3, 3, 6, 6, 5, 5, 5, 5, 3, 3]

# decision variable
x = cp.Variable(len(time_collectors), integer=True) # number of workers start to work at time i

# objective function
obj4 = cp.Minimize(cp.sum(x))

# constraints:
# Each collector works for 4 hours, is off for 1 hour, then works for another 4 hours.
constraints4 = []

# Constraints
for i in range(len(time_collectors)):
    # Active hours for a worker starting at hour i, 9 hour-shift (with 1 hour-break at time 5)
    # do remainder to ensure one-day cycle ((i=23, (i+1)%24 back to i=0)
    working_hours = [i, (i - 1), (i - 2) , (i - 3), (i - 5), (i - 6), (i - 7),
                     (i - 8)]

    # Add constraint for each hour
    constraints4.append(cp.sum(x[working_hours]) >= time_collectors[i])

    constraints4.append(x>=0)

# Solve the problem
prob4 = cp.Problem(obj4, constraints4)
prob4.solve()

# Print the results
print(f"Minimum collectors needed: {prob4.value}")
print("Number of collectors starting at each hour (from 0am - 23pm):")
print(x.value)


######################################################
print(" ")
# P5
print("Problem 5")

print("(a)-(b)")
# decision variables
AS = cp.Variable()
AU = cp.Variable()
BS = cp.Variable()
BU = cp.Variable()
CS = cp.Variable()
CU = cp.Variable()

# objective function
obj5 = cp.Maximize(60*AS + 40*BS + 75*CS + 30*AU + 20*BU + 40*CU)

# constraints
constraints5 = [BS + BU >=20,
		        AU + BU + CU <=50,
		        AS + AU + 0.5*BS + 0.5*BU + 2*CS + 2*CU <=200,
		        4*AS + 4*AU + 3*BS + 3*BU + 6*CS + 6*CU <=700,
		        7*AS + 5*BS + 8*CS <=550,
                AS >= 0, AU>=0, BS>=0, BU >=0, CS>=0, CU>=0]

# solve the problem
prob5 = cp.Problem(obj5, constraints5)
result = prob5.solve()

print(f"Max profit: ${result: .2f}")
print("Stained Model A:", AS.value)
print("Unstained Model A:", AU.value)
print("Stained Model B:", BS.value)
print("Unstained Model B:", BU.value)
print("Stained Model C:", CS.value)
print("Unstained Model C:", CU.value)

print("(c)")
# Extra hours for cutting, assembling, staining
cutting = 200 - (AS.value + AU.value + 0.5*BS.value + 0.5*BU.value + 2*CS.value + 2*CU.value)
assembling = 700- (4*AS.value + 4*AU.value + 3*BS.value + 3*BU.value + 6*CS.value + 6*CU.value)
staining = 550 - (7*AS.value + 5*BS.value + 8*CS.value)

print("Extra hours for cutting:", cutting, "hours")
print("Extra hours for assembling:", assembling, "hours")
print("Extra hours for staining:", staining, "hours")

print("(d)-(g)")
def solve_LP(stained_profit_A, unstained_profit_A, available_cutting, available_assembling):
    # Variables
    AS = cp.Variable(integer=True)
    AU = cp.Variable(integer=True)
    BS = cp.Variable(integer=True)
    BU = cp.Variable(integer=True)
    CS = cp.Variable(integer=True)
    CU = cp.Variable(integer=True)

    # Objective function
    profit = stained_profit_A * AS + unstained_profit_A * AU + 40 * BS + 20 * BU + 75 * CS + 40 * CU
    obj5 = cp.Maximize(profit)

    # Constraints
    constraints5 = [
        AS + AU + 0.5 * (BS + BU) + 2 * (CS + CU) <= available_cutting,
        4 * (AS + AU) + 3 * (BS + BU) + 6 * (CS + CU) <= available_assembling,
        7 * AS + 5 * BS + 8 * CS<= 550,
        BS + BU>= 20,
        AU + BU + CU <=50,
        AS >= 0, AU >= 0, BS >= 0, BU >= 0, CS >= 0, CU >= 0]

    # Solve
    prob = cp.Problem(obj5, constraints5)
    result5 = prob.solve()

    # Return results
    return{
        "profit": result5,
        "AS": AS.value,
        "AU": AU.value,
        "BS": BS.value,
        "BU": BU.value,
        "CS": CS.value,
        "CU": CU.value
    }

# b)
print("\n(b) Original Problem:")
result = solve_LP(stained_profit_A=60, unstained_profit_A=30, available_cutting=200, available_assembling=700)
print(result)

# d) Stained Model A profit margin changes
print("\n(d) Stained Model A profit margin changes:")
for profit in [50, 55, 65, 70]:
    result = solve_LP(stained_profit_A=profit,unstained_profit_A=30, available_cutting=200, available_assembling=700)
    print(f"For stained Model A profit = ${profit}, results = {result}")

# e) Unstained Model A profit margin changes
print("\n(e) Unstained Model A profit margin changes:")
for profit in [20, 25, 35, 40]:
    result = solve_LP(stained_profit_A=60, unstained_profit_A=profit, available_cutting=200, available_assembling=700)
    print(f"For unstained Model A profit = ${profit}, results = {result}")

# f) Cutting hours changes
print("\n(f) Available cutting hours changes:")
for hours in [150, 175, 225, 250]:
    result = solve_LP(stained_profit_A=60, unstained_profit_A=30, available_cutting=hours, available_assembling=700)
    print(f"For available cutting hours = {hours} hrs, results = {result}")

# g) Assembling hours changes
print("\n(g) Available assembling hours changes:")
for hours in [650, 675, 725, 750]:
    result = solve_LP(stained_profit_A=60, unstained_profit_A=30, available_cutting=200, available_assembling=hours)
    print(f"For available assembling hours = {hours} hrs, results = {result}")



######################################################
print(" ")
# P6
print("Problem 6")
# All variables
Gas = ["gas 1", "gas 2", "gas 3"]
Crude = ["Crude 1", "Crude 2", "Crude 3"]
demand = [[4000, 87, 60],
          [3000, 89, 70],
          [2000, 91, 80]]
cost = [[55, 85, 50],
        [65, 90, 65],
        [75, 94, 85]]
trans = 4

# decision variables
x = cp.Variable((len(Gas), len(Crude)), nonneg=True)

# Objective function
costs = [cost[i][0] + trans for i in range(len(Crude))]
obj6 = cp.Minimize(cp.sum(cp.multiply(costs, cp.sum(x, axis=0))))

# Constraints
constraints6 = []

# Gasoline demand
for i in range(len(Gas)):
    constraints6.append(cp.sum(x[i, :]) == demand[i][0])

# Crude constraints
for j in range(len(Crude)):
    constraints6.append(cp.sum(x[:, j]) <= 5000)

# Octane rating
for i in range(len(Gas)):
    constraints6.append(cp.sum(cp.multiply(x[i, :], [cost[j][1] for j in range(len(Crude))])) >= demand[i][0] * demand[i][1])

# Quality rating
for i in range(len(Gas)):
    constraints6.append(cp.sum(cp.multiply(x[i, :], [cost[j][2] for j in range(len(Crude))])) >= demand[i][0] * demand[i][2])

# Solve the problem
prob6 = cp.Problem(obj6, constraints6)
prob6.solve()

# Display the results
print(f"Optimal cost: ${prob6.value: .2f}")
print("Allocation of Crude for each gas (in barrels):")
print(x.value)

