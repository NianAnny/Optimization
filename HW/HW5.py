import numpy as np
import cvxpy as cp

print("Problem 3:")
print("(ii)")
x_3 = cp.Variable(nonneg=True)
y_3 = cp.Variable(nonneg=True)

obj_3 = cp.Maximize(3*x_3 + 2*y_3)

constraints_3 = [2*x_3 - y_3 <= 6,
               2*x_3 + y_3 <= 10]

problem = cp.Problem(obj_3, constraints_3)
problem.solve()

print(f"Optimal value: {problem.value:.0f}")
print(f"Optimal x: {x_3.value:.0f}")
print(f"Optimal y: {y_3.value:.0f}")
##############################################
print("\n(iii)")
print("Iteration 0")
A=np.array([[2,-1,1,0],
             [2,1,0,1]])
c=np.array([3,2,0,0])

basic = [2,3] # initial basis (s1, s2)
nonBasic = [0,1] # initial non-basic variable (x, y)

xB = np.array([6,10])

B=A[:,basic]
N=A[:,nonBasic]

cB=c[basic]
cN=c[nonBasic]

y=np.linalg.solve(np.transpose(B),cB)
cNbar = cN-np.transpose(y) @ N

print(cNbar)

entering = 0
dB=np.linalg.solve(B, -A[:, entering])
print(dB)

ratio = -xB/dB
print(ratio)

# iteration 1
print("\nIteration 1")
basic = [0,3]
nonBasic = [1,2]

xB = np.array([3,4])

B=A[:,basic]
N=A[:,nonBasic]

cB=c[basic]
cN=c[nonBasic]

y=np.linalg.solve(np.transpose(B),cB)
cNbar = cN-np.transpose(y) @ N
print(cNbar)

entering = 1
dB=np.linalg.solve(B, -A[:, entering])
print(dB)

ratio = -xB/dB
print(ratio)

# iteration 2
print("\nIteration 2")
A=np.array([[2,-1,1,0],
             [2,1,0,1]])
c=np.array([3,2,0,0])

basic = [0,1]
nonBasic = [2,3]

xB = np.array([4,2])

B=A[:,basic]
N=A[:,nonBasic]

cB=c[basic]
cN=c[nonBasic]

y=np.linalg.solve(np.transpose(B),cB)
cNbar = cN-np.transpose(y) @ N
print(cNbar)

entering = 2
dB=np.linalg.solve(B, -A[:, entering])
print(dB)

ratio = -xB/dB
print(ratio)

# iteration 3
print("\nIteration 3")
A=np.array([[2,-1,1,0],
             [2,1,0,1]])
c=np.array([3,2,0,0])

basic = [1,2]
nonBasic = [0,3]

xB = np.array([10,16])

B=A[:,basic]
N=A[:,nonBasic]

cB=c[basic]
cN=c[nonBasic]

y=np.linalg.solve(np.transpose(B),cB)
cNbar = cN-np.transpose(y) @ N
print(cNbar, "all negative") # all negative, done!
###################################
print("\nProblem 4 (b)")
print("Iteration 0")
A=np.array([[-5,3,1,0],
            [3,-5,0,1]])
c=np.array([10,-1,0,0])

basic = [1,3]
nonBasic = [0,2]

xB = np.array([5,33])

B=A[:,basic]
N=A[:,nonBasic]

cB=c[basic]
cN=c[nonBasic]

y=np.linalg.solve(np.transpose(B),cB)
cNbar = cN-np.transpose(y) @ N
print(cNbar)

entering = 0
dB=np.linalg.solve(B, -A[:, entering])
print(dB)

ratio = -xB/dB
print(ratio)
###################################################
print("\nProblem 5")
print("(a)")
x1=cp.Variable(nonneg=True)
x2=cp.Variable(nonneg=True)
x3=cp.Variable(nonneg=True)
obj_5=cp.Minimize(3*x1 + 6*x2 + 2*x3)
constraints_5 = [x1 + 3*x2 + 2*x3 >= 6,
                 2*x1 + x2 + x3 >= 3,]
prob_5=cp.Problem(obj_5, constraints_5)
prob_5.solve()
print(f"Optimal value: {prob_5.value}")
print(f"(x1, x2, x3) = {x1.value, x2.value, x3.value}")
############################
print("\n(b)-(c)")
print("Iteration 0")
A=np.array([[1,3,2,-1,0,1,0],
            [2,1,1,0,-1,0,1]])
c=np.array([3,6,2,0,0,0,0])

basic = [5,6]
nonBasic = [0,1,2,3,4]

xB = np.array([6,3])

B=A[:,basic]
N=A[:,nonBasic]

cB=c[basic]
cN=c[nonBasic]

y=np.linalg.solve(np.transpose(B),cB)
cNbar = cN-np.transpose(y) @ N

print(cNbar)

entering = 1
dB=np.linalg.solve(B, -A[:, entering])
print(dB)

ratio = -xB/dB
print(ratio)

print("\nIteration 1")
A=np.array([[1,3,2,-1,0,1,0],
            [2,1,1,0,-1,0,1]])
c=np.array([3,6,2,0,0,0,0])

basic = [1,4]
nonBasic = [0,2,3,5,6]

xB = np.array([2,-1])

B=A[:,basic]
N=A[:,nonBasic]

cB=c[basic]
cN=c[nonBasic]

y=np.linalg.solve(np.transpose(B),cB)
cNbar = cN-np.transpose(y) @ N

print(cNbar)

entering = 2
dB=np.linalg.solve(B, -A[:, entering])
print(dB)

ratio = -xB/dB
print(ratio)

print("\nIteration 2")
A=np.array([[1,3,2,-1,0,1,0],
            [2,1,1,0,-1,0,1]])
c=np.array([3,6,2,0,0,0,0])

basic = [0,2]
nonBasic = [1,3,4,5,6]

xB = np.array([0,3])

B=A[:,basic]
N=A[:,nonBasic]

cB=c[basic]
cN=c[nonBasic]

y=np.linalg.solve(np.transpose(B),cB)
cNbar = cN-np.transpose(y) @ N

print(cNbar)

entering = 0
dB=np.linalg.solve(B, -A[:, entering])
print(dB)

ratio = -xB/dB
print(ratio)























