import numpy as np

# Basic solutions
A = np.array([[4,6,1,0,0],
              [2,6,0,1,0],
              [0,1,0,0,1]])

b = np.array([120,72,10])

basicVars = np.array([2,3,4])
B = A[:,basicVars]

sol = np.linalg.solve(B,b)
print(sol)
#############################################

A = np.array([[4,6,1,0,0],
             [2,6,0,1,0],
             [0,1,0,0,1]])

b = np.array([120,72,10])

c = np.array([2,4,0,0,0])

basis = [1,2,3] # current basis (y,s1,s2)

B = A[:,basis]

# x-simplex direction
dx = np.linalg.solve(B,-A[:,0])

# s3-simplex direction
ds3 = np.linalg.solve(B,-A[:,4])

print(dx,ds3)

# check if dx is improving
dxFull = np.array([1,dx[0],dx[1],dx[2],0])
ds3Full = np.array([0,ds3[0],dx[1],dx[2],1])

print(np.dot(c,dxFull)) # introducing x improves the objective
print(np.dot(c,ds3Full))

# choose x as the simplex direction, use ratio test to choose stepsize
xB = [10,60,12]
l = min([-xB[i+1]/dx[i+1] for i in range(2)])
print(l)
########################################################

# Efficient Simplex
print("\n")
A = np.array([[1,1,1,0,0],
             [5,2,0,1,0],
             [0,1,0,0,1]])

c = np.array([10,3,0,0,0])

xB = np.array([10, 60, 12])

basicVars = [1,2,3]
nonbasicVars = [0,4]

B = A[:,basicVars]
N = A[:,nonbasicVars]

cB = c[basicVars]
cN = c[nonbasicVars]

y = np.linalg.solve(np.transpose(B),cB)
print(y)

cNbar = cN - np.transpose(y) @ N
print(cNbar)

entering = 2
dB = np.linalg.solve(B,-A[:,entering])
print(dB)

ratios = -xB / dB
print(ratios)






