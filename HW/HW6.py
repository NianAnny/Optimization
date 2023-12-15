import cvxpy as cp
import numpy as np

print("Problem 1")
print("(a)")
x1= cp.Variable(nonneg=True)
x2= cp.Variable(nonneg=True)
x3= cp.Variable(nonneg=True)
obj_a=cp.Maximize(8*x1+20*x2+4*x3)
con_a = [2*x1 + 3*x2 + 2*x3 <= 20,
         x2 + x3 <= 8,
         3*x1 + x2 - 4*x3 >=10]
prob_a=cp.Problem(obj_a, con_a)
prob_a.solve()

y=cp.Variable(3)
obj_ay = cp.Minimize(20*y[0]+8*y[1]+10*y[2])
con_ay=[2*y[0]+3*y[2]>=8,
        3*y[0]+y[1]+y[2]>=20,
        2*y[0]+y[1]-4*y[2]>=4,
        y[0]>=0,
        y[1]>=0]
prob_ay = cp.Problem(obj_ay, con_ay)
prob_ay.solve()
print("Testify to the optimal value:")
print(prob_a.value)
print(prob_ay.value)
###################################
print("(b)")
x_b=cp.Variable(4)
obj_bx = cp.Maximize(30*x_b[0]+2*x_b[2]+10*x_b[3])
con_bx=[2*x_b[0]-3*x_b[1]+9*x_b[3]<=10,
        4*x_b[1]-x_b[2]>=19,
        x_b[0]+x_b[1]+x_b[2]==5,
        x_b[0]>=0,
        x_b[2]<=0]
prob_bx = cp.Problem(obj_bx, con_bx)
prob_bx.solve()

y_b=cp.Variable(3)
obj_by=cp.Minimize(10*y_b[0]+19*y_b[1]+5*y_b[2])
con_by=[2*y_b[0]+y_b[2]>=30,
        -3*y_b[0]+4*y_b[1]+y_b[2]==0,
        -y_b[1]+y_b[2]<=-2,
        9*y_b[0]==10,
        y_b[0]>=0,
        x_b[2]<=0]
prob_by=cp.Problem(obj_by, con_by)
prob_by.solve()
print("Testify to the optimal value:")
print(prob_bx.value)
print(prob_by.value)
###########################################
print("\nProblem 2")
print("(c)")
print("Iteration 0")
A = np.array([[1,1,1,0],
             [1,-1,0,1]])
c = np.array([5,1,0,0])
xB = np.array([7,3])

basicVars = [2,3]
nonbasicVars = [0,1]

B = A[:,basicVars]
N = A[:,nonbasicVars]

cB = c[basicVars]
cN = c[nonbasicVars]

y = np.dot(np.linalg.inv(B.T), cB)

cNbar = cN - np.dot(np.transpose(y), N)
print(cNbar)

entering = 0
dB = np.linalg.solve(B,-A[:,entering])
print(dB)

ratios = -xB / dB
print(ratios)

print("Iteration 1")
A = np.array([[1,1,1,0],
             [1,-1,0,1]])
c = np.array([5,1,0,0])

xB = np.array([3,4])

basicVars = [0,2]
nonbasicVars = [1,3]

B = A[:,basicVars]
N = A[:,nonbasicVars]

cB = c[basicVars]
cN = c[nonbasicVars]

y = np.dot(np.linalg.inv(B.T), cB)

cNbar = cN - np.dot(np.transpose(y), N)
print(cNbar)

entering = 1
dB = np.linalg.solve(B,-A[:,entering])
print(dB)

ratios = -xB / dB
print(ratios)

print("Iteration 2")
A = np.array([[1,1,1,0],
             [1,-1,0,1]])
c = np.array([5,1,0,0])

xB = np.array([5,2])

basicVars = [0,1]
nonbasicVars = [2,3]

B = A[:,basicVars]
N = A[:,nonbasicVars]

cB = c[basicVars]
cN = c[nonbasicVars]

y = np.dot(np.linalg.inv(B.T), cB)

cNbar = cN - np.dot(np.transpose(y), N)
print(cNbar)
####################################
print("\n(d)")
print("Iteration 0")
A = np.array([[1,1,-1,0],
             [1,-1,0,-1]])
c = np.array([7,3,0,0])
xB = np.array([5,4])

basicVars = [0,3]
nonbasicVars = [1,2]

B = A[:,basicVars]
N = A[:,nonbasicVars]

cB = c[basicVars]
cN = c[nonbasicVars]

y = np.dot(np.linalg.inv(B.T), cB)

cNbar = cN - np.dot(np.transpose(y), N)
print(cNbar)

entering = 1
dB = np.linalg.solve(B,-A[:,entering])
print(dB)

ratios = -xB / dB
print(ratios)

print("Iteration 1")
A = np.array([[1,1,-1,0],
             [1,-1,0,-1]])
c = np.array([5,1,0,0])

xB = np.array([3,2])

basicVars = [0,1]
nonbasicVars = [2,3]

B = A[:,basicVars]
N = A[:,nonbasicVars]

cB = c[basicVars]
cN = c[nonbasicVars]

y = np.dot(np.linalg.inv(B.T), cB)

cNbar = cN - np.dot(np.transpose(y), N)
print(cNbar)
#############################################
print("\nProblem 5")
# Primal: n decision variables and m constraints
#         0: minimization; 1: maximization
#
def Dual_Function(obj_type, c, A, b, constraints, variables):
    dual_obj_type = 1 - obj_type # determine the dual objective type based on that of the primal
    c_dual = b # b transpose of the primal returns objective of dual

    # A_dual = A transpose;,
    A_dual = A.T

    b_dual = c # c of the primal returns constraints of the dual
    dual_constriants = variables # check direction of dual constraints based on primal variables' direction

    # Check dual varables' directions based on primal constraints' direction
    dual_variables = -1 * constraints

    return{
        'Dual type': dual_obj_type,
        'Dual objective vector': c_dual,
        'Dual constraint coefficient matrix': A_dual,
        'Dual RHS': b_dual,
        'Dual constraint direction': dual_constriants,
        'Dual decision variable direcion': dual_variables
    }

#


# Test code
# Problem 1 (a)
obj_type = 1
c = np.array([8, 20, 4])
A = np.array([[2, 3, 2],
              [0, 1, 1],
              [3, 1, -4]])
b = np.array([20, 8, 10])
constraints = np.array([-1, -1, 1])
variables = np.array(([1, 1, 1]))
Dual = Dual_Function(obj_type=obj_type, c=c, A=A, b=b, constraints=constraints, variables=variables)
print(f"Check for problem 1(a):{Dual}")

# Problem 1 (b)
obj_type_b = 1
c_b = np.array([30, 0, -2, 10])
A_b = np.array([[2, -3, 0, 9],
              [0, 4, -1, 0],
              [1, 1, 1, 0]])
b_b = np.array([10, 19, 5])
constraints_b = np.array([-1, 1, 0])
variables_b = np.array(([1, 0, -1, 0]))
Dual = Dual_Function(obj_type=obj_type_b, c=c_b, A=A_b, b=b_b, constraints=constraints_b, variables=variables_b)
print(f"\nCheck for problem 1(b):{Dual}")







































