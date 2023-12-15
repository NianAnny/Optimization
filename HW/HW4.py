import cvxpy as cp
import numpy as np

print("Problem 1:")
# Variables
Plant = ["Plant 1", "Plant 2", "Plant 3"]
City = ["City 1", "City 2", "City 3", "City 4"]
costs = np.array([[8, 6, 10, 9],
                [9, 12, 13, 7],
                [14, 9, 16, 5]])
Supply = [35, 50, 40]
Demand = [45, 20, 30, 30]

# Define the decision variable as plant i (row) to city j (column)
x = cp.Variable((len(Plant), len(City)), nonneg=True)

# Objective
# Minimize the total cost of every transportation (plant i -> city j)
obj_1 = cp.Minimize(cp.sum(cp.multiply(costs, x)))

# Constraints
constraints_1 = []

# Supply constraints
for i in range(len(Plant)):
    constraints_1.append(cp.sum(x[i, :]) <= Supply[i])

# Demand constraints
for j in range(len(City)):
    constraints_1.append(cp.sum(x[:, j]) == Demand[j])

# Solve the problem
prob_1 = cp.Problem(obj_1, constraints_1)
prob_1.solve()

# print results
print(f"Optimal Cost: ${prob_1.value:.2f}")
print("Electricity Distribution (million kwh):")
print(x.value)
for i in range(len(Plant)):
    for j in range(len(City)):
        print(f"{Plant[i]} -> {City[j]}: {x.value[i,j]:.2f}")

################################################################
print("\nProblem 2:")
# Variables
capacity = [200, 240, 180, 210, 270, 390]
demand = [80, 40, 50, 65, 90, 30, 75, 20, 45, 60, 40, 55]
cost_matrix = np.array([[20, 35, 48, 0, 0, 0, 37, 22, 18, 30, 45, 35],
              [27, 55, 62, 45, 20, 18, 0, 0, 15, 32, 27, 20],
              [0, 0, 25, 30, 45, 60, 15, 50, 40, 30, 40, 50],
              [0, 25, 35, 50, 40, 20, 15, 30, 35, 0, 0, 25],
              [45, 0, 0, 0, 35, 50, 40, 20, 30, 15, 20, 0],
              [30, 30, 30, 45, 0, 55, 40, 30, 45, 30, 0, 40]])
# Replace zeros in the cost_matrix with a large number (huge cost) to simulate the constraint
# that those delivery channels are not allowed.
cost_matrix[cost_matrix == 0] = 100000000
thousands = 1000 # cost in $1000s

# decision variable
x_2 = cp.Variable((len(capacity), len(demand)), nonneg=True)

# objective function
obj_2 = cp.Minimize(cp.sum(cp.multiply(cost_matrix, x_2)))

# constraints
constraints_2 = []

# deport capacity
for i in range(len(capacity)):
    constraints_2.append(cp.sum(x_2[i, :]) <= capacity[i])

# customer demand
for j in range(len(demand)):
    constraints_2.append(cp.sum(x_2[:, j]) == demand[j])

prob_2 = cp.Problem(obj_2, constraints_2)
prob_2.solve()

print(f"Optimal cost: ${prob_2.value * thousands:.2f}")
print("Shipment Distribution:\n", x_2.value)
for i in range(len(capacity)):
    for j in range(len(demand)):
        if x_2.value[i, j] > 0.0001:
            print(f"Depot {i+1} -> Customer {j+1}: {x_2.value[i, j]:.2f}")

#################################################################
print("\nProblem 3:")
# Define the variables
x_3 = cp.Variable(12, boolean=True)

# Objective
obj_3 = cp.Maximize(cp.sum(x_3))

# Constraints (continuing from your initial problem statement)
constraints_3 = [
    x_3[0] + x_3[2] + x_3[4] + x_3[6] + x_3[7] + x_3[8] <= 1,
    x_3[1] + x_3[7] + x_3[8] <= 1,
    x_3[0] + x_3[3] + x_3[6] + x_3[7] + x_3[8] <= 1,
    x_3[3] + x_3[9] <= 1,
    x_3[0] + x_3[3] + x_3[5] <= 1,
    x_3[5] + x_3[9] + x_3[10] <= 1,
    x_3[0] + x_3[2] + x_3[4] + x_3[6] + x_3[11] <= 1,
    x_3[0] + x_3[1] + x_3[2] + x_3[7] + x_3[8] <= 1,
    x_3[3] + x_3[5] + x_3[9] + x_3[10] + x_3[11] <= 1
]

# Solve the problem
prob_3 = cp.Problem(obj_3, constraints_3)
prob_3.solve()

print("Optimal Value:", prob_3.value)
print("Solution set:", x_3.value)
for i in range(12):
    print(f"x{i+1}: {x_3.value[i]:.0f}")

################################################################
print("\nProblem 4: Show in doc.")




###############################################################
print("\nProblem 5: Show in doc.")











