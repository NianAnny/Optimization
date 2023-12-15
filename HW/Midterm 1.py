import cvxpy as cp
import matplotlib.pyplot as plt
import numpy as np

print("Problem 1:")
# States number of people in each subfamily
subfamily = [range(0, 2), # first subfamily
             range(2, 7), # second subfamily
             range(7, 14), # third subfamily
             range(14, 21)] # fourth subfamily
members = sum((len(subfamilies) for subfamilies in subfamily))

# Define decision variable
x_1 = cp.Variable((members, members), boolean=True)

# objective function
# For a well-mixed cycle, define a connection as the sum of gifts between subfamilies
connections = cp.sum([x_1[i, j] for sub_i in subfamily for sub_j in subfamily for i in sub_i for j in sub_j if sub_i != sub_j])
obj_1 = cp.Minimize(connections)

# constraints
constraints_1 = []

# one to one gift-flow
for i in range(members): # giving
    constraints_1.append(cp.sum(x_1[i, :]) == 1)

for j in range(members): # receiving
    constraints_1.append(cp.sum(x_1[:, j]) == 1)

# ensure nobody buys a gift to someone in the same subfamily (as well as not buying for themselves)
for families in subfamily:
    for i in families:
        for j in families:
            constraints_1.append(x_1[i, j] == 0)

# solve for the problem
prob_1a = cp.Problem(obj_1, constraints_1)
prob_1a.solve()
# print(x_1.value)
print("(a)")
for i in range(members):
    for j in range(members):
        if x_1[i, j].value == 1:
            print(f"Person {i+1} buys a gift for person {j+1}")

##########################
print("\n(b)")
# According to the previous solution, adding a new constraint to ensure that person 1 won't buy a gift for person 6 at this time
constraints_1.append(x_1[0, 5] == 0)
# constraints_1.append(x_1[2, 20] == 0)

prob_1b = cp.Problem(obj_1, constraints_1)
prob_1b.solve()

for i in range(members):
    for j in range(members):
        if x_1[i, j].value == 1:
            print(f"Person {i+1} buys a gift for person {j+1}")

###########################
print("\n(c)")
# Construct a generalized function for the algorithm
def gift_assignment(family_size):
    # Instead of stating each subfamily members, construct a subfamily range directly
    subfamily_1c = []
    for size in family_size:
        subfamily_1c.append(range(0, 0 + size))
    members_1c = sum(family_size)

    x_1c = cp.Variable((members_1c, members_1c), boolean=True) # decision variable

    # objecive function
    connections_1c = cp.sum([x_1c[i, j] for sub_i in subfamily for sub_j in subfamily for i in sub_i for j in sub_j if sub_i != sub_j])
    obj_1c = cp.Minimize(connections_1c)

    # Constraints
    constraints_1c = []

    # buying and receiving
    for i in range(members_1c):  # buying
        constraints_1c.append(cp.sum(x_1c[i, :]) == 1)

    for j in range(members_1c):  # receiving
        constraints_1c.append(cp.sum(x_1c[:, j]) == 1)

    # Ensure nobody buys a gift for someone (include himself/herself) in the same subfamily
    for family in subfamily_1c:
        for i in family:
            for j in family:
                constraints_1c.append(x_1c[i, j] == 0)

    # Solve for the problem
    prob_1c = cp.Problem(obj_1c, constraints_1c)
    prob_1c.solve()

    # Print results
    assignment = []
    for i in range(members_1c):
        for j in range(members_1c):
            if x_1c[i, j].value == 1:
                assignment.append((i + 1, j + 1))

    return assignment
# end function

# solve the problem with any number m subfamilies
# 6 subfamilies of size 1, 2, 5, 5, 6, 2
family_size = [1, 2, 5, 5, 6, 2]
gift_assignments = gift_assignment(family_size)
for buyer, receiver in gift_assignments:
    print(f"Person {buyer} buys a gift for person {receiver}")

#####################################################################
print('\n\nProblem 2:')
print("(a): see in doc.")
#####################
print("\n(b): see in doc.")
# set days in Iowa is x-axis and days in Kansas is y-axis
I_days = np.linspace(0, 200, 400)

# Represent days in Kansas by I_days
K_days_1 = (18000-120*I_days)/100
I_days_1 = 50
K_days_2 = 60
K_days_3 = 365-I_days

# plot each constraint
plt.plot(I_days, K_days_1, label=r"$120x + 100y \leq 18000$")
plt.axvline(x=50, color = "red", label=r"$x \geq 50 $")
plt.axhline(y=60, color = "green", label=r"$y \geq 60 $")
plt.plot(I_days, K_days_3, label=R"$ x + y \leq 365$")

# feasible region
lwr = np.maximum(I_days_1, K_days_2)
plt.fill_between(I_days, K_days_1, lwr, where=((I_days >= I_days_1) & (K_days_1 >= lwr)), alpha=0.5)

# plotting
plt.xlim(0, 150)
plt.ylim(0, 365)
plt.xlabel("Days in Iowa")
plt.ylabel("Days in Kansas")
plt.legend()
plt.show()

###################
print("\n(c)")
# define the decision variable
I_day = cp.Variable()
K_day = cp.Variable()

# objective
obj_2 = cp.Maximize(3000*I_day + 2500*K_day)

# constraints
constraints_2 = [120*I_day + 100*K_day <= 18000,
                 I_day >= 50,
                 K_day >= 60,
                 I_day >= 0,
                 K_day >= 0]

prob_2 = cp.Problem(obj_2, constraints_2)
prob_2.solve()
print(f"Optimal sales: ${prob_2.value}")
print(f"Stay in Iowa for {I_day.value} days and in Kansas for {K_day.value} days.")

######################
print("\n(d): see in doc.")

####################################################################
print('\n\nProblem 3 (a-b): see in doc.')

###################################################################
print('\n\nProblem 4:')
print("(a): see in doc.")

print("\n(b)")
# All variables
Plants = ["Plant 1", "Plant 2", "Plant 3"]
Distributors =["Distributor 1", "Distributor 2"]
Stores = ["Store 1", "Store 2", "Store 3"]
Supply = [1000, 750, 500]
Demand = [700, 600, 800]
distribution_cost = np.array([[8, 14],
                              [12, 10],
                              [16, 12]])
store_cost = np.array([[10, 8, 12],
                      [6, 15, 9]])

# Decision variables, ensure they are non-negative
x_4 = cp.Variable((len(Plants), len(Distributors)), nonneg=True)
y_4 = cp.Variable((len(Distributors), len(Stores)), nonneg=True)

# objective
cost = cp.sum(cp.multiply(distribution_cost, x_4)) + cp.sum(cp.multiply(store_cost, y_4))
obj_4 = cp.Minimize(cost)

# constraints
constraints_4 =[]

# supply
for i in range(len(Plants)):
    constraints_4.append(cp.sum(x_4[i, :]) <= Supply[i])

# demand
for k in range(len(Stores)):
    constraints_4.append(cp.sum(y_4[:, k]) == Demand[k])

# transporting distribution
for j in range(len(Distributors)):
    constraints_4.append(cp.sum(x_4[:, j]) == cp.sum(y_4[j, :]))

# solve the problem
prob_4 = cp.Problem(obj_4, constraints_4)
prob_4.solve()
print(f"Optimal transporting cost is ${prob_4.value:.2f}")
print(f"\nPlants to Distributors: \n{x_4.value}")
for i in range(len(Plants)):
    for j in range(len(Distributors)):
        print(f"{Plants[i]} to {Distributors[j]}: {x_4[i,j].value:.0f}")
print(f"\nDistributors to Stores: \n{y_4.value}")
for j in range(len(Distributors)):
    for k in range(len(Stores)):
        print(f"{Distributors[j]} to {Stores[k]}: {y_4[j,k].value:.0f}")

#####################
print("\n(c)")
Plants = ["Plant 1", "Plant 2", "Plant 3"]
Distributors =["Distributor 1", "Distributor 2"]
Stores = ["Store 1", "Store 2", "Store 3"]
Stores_plus = ["Store 1", "Store 2", "Store 3"]
distribution_cost = np.array([[8, 14],
                              [12, 10],
                              [16, 12]])
store_cost = np.array([[10, 8, 12],
                      [6, 15, 9]])
Supply_c = [1000*2, 750*2, 500*2]
Demand_type_1 = [700, 600, 800]
Demand_type_2 = [500, 900, 700]
truck_limit = 1000

# decision variables
x_4c = cp.Variable((len(Plants), len(Distributors)), nonneg=True)
y_4c = cp.Variable((len(Distributors), len(Stores)), nonneg=True)
y_4c_2 = cp.Variable((len(Distributors), len(Stores_plus)), nonneg=True) # transportation for beer 2

# objective
obj_4c = cp.Minimize(cp.sum(cp.multiply(distribution_cost, x_4c))
                    + cp.sum(cp.multiply(store_cost, y_4c))
                    + cp.sum(cp.multiply(store_cost, y_4c_2)))

# constraints
constraints_4c =[]

# Supply
for i in range(len(Plants)):
    constraints_4c.append(cp.sum(x_4c[i, :]) <= Supply_c[i])

# Demand
for k in range(len(Stores)):
    constraints_4c.append(cp.sum(y_4c[:, k]) == Demand_type_1[k]) # for type 1
for k in range(len(Stores_plus)):
    constraints_4c.append(cp.sum(y_4c_2[:, k]) == Demand_type_2[k]) # for type 2

# transportation
for j in range(len(Distributors)):
    constraints_4c.append(cp.sum(x_4c[:, j]) == cp.sum(y_4c[j, :]) + cp.sum(y_4c_2[j, :]))

# truck limit
for j in range(len(Distributors)):
    for k in range(len(Stores)):
        constraints_4c.append(cp.sum(y_4c[j, k]) + cp.sum(y_4c_2[j, k]) <= truck_limit)

# solve the problem
prob_4c = cp.Problem(obj_4c, constraints_4c)
prob_4c.solve()
print(f"Optimal transporting cost is ${prob_4c.value:.2f}")
print(f"\nPlants to Distributors: \n{x_4c.value}")
for i in range(len(Plants)):
    for j in range(len(Distributors)):
        print(f"{Plants[i]} to {Distributors[j]}: {x_4c[i,j].value:.0f}")
print(f"\nDistributors to Stores for type 1 beer: \n{y_4c.value} ")
for j in range(len(Distributors)):
    for k in range(len(Stores)):
        print(f"{Distributors[j]} to {Stores[k]}: {y_4c[j,k].value:.0f}")
print(f"\nDistributors to Stores for type 2 beer: \n{y_4c_2.value}")
for j in range(len(Distributors)):
    for k in range(len(Stores_plus)):
        print(f"{Distributors[j]} to {Stores_plus[k]}: {y_4c_2[j, k].value:.0f}")



































