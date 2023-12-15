import cvxpy as cp
import numpy as np

print("Problem 1")
def Simplex_Method(c, A, b):
    print("\n===============================") # a signal for solving a new problem
    # Parameters:
    # c: objective vector (n * 1)
    # A: coefficient constraint matrix (m * n)
    # b: constraint vector (m * 1)

    # Wants to return the optimal objective value and the solution vector

    # Check that inputs have consistent dimensions
    m, n = A.shape  # count number of constraints (m), and number of variables (n)
    if len(b) != m or len(c) != n:
        return ("The input is inconsistent.")

    # Check the feasibility of initial solution at origin
    x_origin = np.array(np.zeros(n)) # assume all variables are zeros
    Ax = A @ x_origin
    if np.any(Ax > b):
         return (f"The initial solution at {x_origin} is infeasible!")

    # Add slack/surplus variables forming the canonical form
    c_s = np.hstack([c, np.zeros(m)]) # add 0s as slack coefficient
    A_s = np.hstack([A, np.identity(m)]) # add an identity matrix for slacks

    # Check for Basis and nonBasis indices in coefficient matrix
    # Convert the standard form to canonical form
    basicVars = list(range(n, n + m)) # slacks' indices
    nonBasicVars = list(range(n)) # variables' indices

    # Initialization
    # create x vector as the same length as that of n variables including slacks (n+m)
    x = np.zeros(n + m)
    x[basicVars] = b  # construct a vector contains all variables values so far

    iteration = 100 # set up max iteration to avoid infinite loops

    for i in range(iteration):
        # Ensure order of variables is correct
        basicVars = sorted(basicVars)
        nonBasicVars = sorted(nonBasicVars)

        B = A_s[:, basicVars] # basis of coefficient matrix
        N = A_s[:, nonBasicVars] # nonBasis of coefficient matrix
        cB = c_s[basicVars] # basic objective vector
        cN = c_s[nonBasicVars] # nonBasic objective vector
        xB = x[basicVars] # basic variable values
        b = xB # define basic variable vector

        # Step 1: Compute simplex multipliers (y) and reduced costs (cNbar)
        y = np.linalg.solve(np.transpose(B), cB)
        cNbar = cN - np.transpose(y) @ N

        # Check for the optimality
        if np.all(cNbar <= 0): # reach the optimum
            break

        # Step 2: Compute the reduced cost
        if np.any(cNbar > 0):
            # Store the results of the current iteration
            x = x  # store basic variable values, nonBasic ones are 0

        # Step 3: Compute simplex direction
        entering_index = np.argmax(cNbar) # check for the index of the variable direction we will choose
        entering = nonBasicVars[entering_index] # the entering variable index
        dB = np.linalg.solve(B, -A_s[:, entering]) # direction

        # Check for unboundedness
        if np.all(dB >= 0):
            return ("Detect that the problem is unbounded!")

        print(f"Iteration_{i}:")
        print(f"Start at {x}")  # start point for iteration_i

        # Step 4: Compute maximum step size
        steps = np.where(dB < 0, -b/dB, np.inf) # available step sizes,
        step_max = np.min(steps) # select the max step value

        leaving_index = np.argmin(steps) # define the leaving variable's index
        leaving = basicVars[leaving_index] # define the leaving variable

        # Step 5: Update the solution and basis
        b = b + step_max * dB # basic variable values change
        x[sorted(basicVars)] = b # current values for basic variables
        b[leaving_index] = step_max  # new basic variable values

        # replace leaving variable with nonBasic entering and entering with leaving in the solution vector
        basicVars[leaving_index] = entering
        nonBasicVars[entering_index] = leaving

        # Store the results of the current iteration, renew the solution
        x[basicVars] = b
        optimal_value = c_s @ x # calculate the optimal value

        # Check B, N, cB, cN, xB for the current iteration
        print(f"B: {B}")
        print(f"N: {N}")
        print(f"cB: {cB}")
        print(f"cN: {cN}")
        print(f"xB: {xB}")

        # check for reduced cost, entering variable, direction, max step for the current iteration
        print(f"reduced cost (cNbar): {cNbar}, entering: c_{entering}")
        print(f"dB: {dB}")
        print(f"lambda: {steps}, select lambda_max: {step_max}")

        # Check for objective value and point for the current iteration
        print(f"Current point: {x}")
        print(f"Objective value: {optimal_value}")
        print("\n-------------------------------") # a signal of another iteration or the solution

        # Return the optimal value and the corresponding point
    return {"Optimal value": optimal_value,
            "Solution vector": x}
A = np.array([[1,-11,-5,18],
              [1,-3,-1,2],
              [1,0,0,0,]])
c = np.array([10,-57,-9,-24])
# iteration
b = np.array([0,0,1])
outcome = Simplex_Method(c, A, b)
print(f"{outcome}")
################################################

print("\nProblem 2")
c = np.array([2,5,0,0,0])
A = np.array([[-1,2,0,-1,1],
              [0,-1,1,1,0]])
b = np.array((-2,0))

basic = [0,3]
nonbasic = [1,2,4]

B = A[:, basic]
N = A[:, nonbasic]

cB = c[basic]
cN = c[nonbasic]

y = np.linalg.solve(np.transpose(B),cB)
print(y)

cNbar = cN - np.transpose(y) @ N
print(cNbar)

entering = 1
dB = np.linalg.solve(B,-A[:,entering])
print(dB)

ratios = -b / dB
print(ratios)
#################################################

print("\nProblem 3")
A = np.array([[3,1,4,4],
              [4,2,5,5],
              [5,5,4,0]])
c=np.array([20,25,50,30])
b = np.array([150,185,250])
outcome = Simplex_Method(c, A, b)
print(outcome)
################################################

print("\nProblem 5")
machine_time_available = 60 * 60  # hours to minutes
variable_costs = [30, 10, 10, 20]  # per thickness
fixed_costs = [25/60, 25/60, 35/60]  # labor cost per (hr to min) for each machine
revenues = [110, 90, 60, 100]  # in dollars
max_demand = [400, 250, 200, 450]  # in square yards
machine_time = [[5, 8, 9],
                [4, 7, 5],
                [4, 5, 4],
                [6, 10, 6]] # in minutes

# Decision variables for the number of square yards to produce for each thickness
x = cp.Variable(4, nonneg=True)

totalRevenue = cp.sum([revenues[i] * x[i] for i in range(4)])
totalVariableCost = cp.sum([variable_costs[i] * x[i] for i in range(4)])
totalFixedCost = cp.sum([fixed_costs[j] * cp.sum([machine_time[i][j] * x[i] for i in range(4)]) for j in range(3)])

# Maximize profit
profit = totalRevenue - (totalVariableCost + totalFixedCost)
objective = cp.Maximize(profit)

# Constraints
constraints = []
for j in range(3):
    constraints.append(cp.sum([machine_time[i][j] * x[i] for i in range(4)]) <= machine_time_available)

for i in range(4):
    constraints.append(x[i] <= max_demand[i])

# Define the problem and solve it
problem = cp.Problem(objective, constraints)
problem.solve()

print(f"Optimal value (profit): ${problem.value:.2f}")
print(f"Production plan (square yards): {x.value}")
for i in range(len(constraints)):
    print(f"Shadow prices for constraints: {constraints[i].dual_value}")


revenues = [110, 90, 60, 100+33.74]  # in dollars
x = cp.Variable(4, nonneg=True)
totalRevenue = cp.sum([revenues[i] * x[i] for i in range(4)])
totalVariableCost = cp.sum([variable_costs[i] * x[i] for i in range(4)])
totalFixedCost = cp.sum([fixed_costs[j] * cp.sum([machine_time[i][j] * x[i] for i in range(4)]) for j in range(3)])
# Maximize profit
profit = totalRevenue - totalVariableCost - totalFixedCost
objective = cp.Maximize(profit)
# Constraints
constraints = []
for j in range(3):
    constraints.append(cp.sum([machine_time[i][j] * x[i] for i in range(4)]) <= machine_time_available)
for i in range(4):
    constraints.append(x[i] <= max_demand[i])
# Define the problem and solve it
problem = cp.Problem(objective, constraints)
problem.solve()
print(f"\nOptimal value (profit): ${problem.value:.2f}")
print(f"Production plan (square yards): {x.value}")




























