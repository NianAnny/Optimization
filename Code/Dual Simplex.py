import numpy as np

# inputs to dual simplex would be: the linear program c,A,b, an initial infeasible xB and its complementary slackness counterpart yB

A = np.array([[4,6,1,0,0,0],
             [2,6,0,1,0,0],
             [0,1,0,0,1,0],
             [1,0,0,0,0,1]])

c = np.array([2,4,0,0,0,0])

# full x (x1,x2,s1,s2,s3,s4)
xFull = np.array([24.,4,0,0,6,-4])

# full y reordered to coincide with x for ease of comp. slackness (w1,w2,y1,y2,y3,y4)
yFull = np.array([0,0,1/3,1/3,0,0])

# primal basis and nonbasis
primalBasis = [0,1,4,5]
primalNonbasis = [2,3]

# all the nonzero entries of x and y
xB = xFull[primalBasis]
yB = yFull[primalNonbasis]


# construct basic / nonbasic parts of constraint matrix A
B = A[:,primalBasis]
N = A[:,primalNonbasis]

# entering variable in dual / leaving variable in primal is dictated by cNbar, which is just xB!
cNbar = xB
print(cNbar)

# inspect the above to choose entering dual / leaving primal
leavingPrimal = 5 # the only negative value is primalBasis[3] = variable 5 (s4)
leavingPrimalBasis = 3 # s4 corresponds to variable 4 in the basis

# step size for the primal can be read off of xB
lambdaPrimal = -xFull[leavingPrimal]

# simplex direction for dual comes from taking the associated row of B^-1*N - note that variable 5 (s4) corresponds to the 4th entry in the basis
BinvN = np.dot(np.linalg.inv(B),N)
dBhat = BinvN[leavingPrimalBasis,:]

# use ratio test to pick leaving dual aka entering primal
dualRatios = -yB / dBhat
print(dualRatios)

# inspect the ratio test above to pick the leaving dual / entering primal
enteringPrimal = 3 # 2nd entry in N corresponds to s1
newPrimalBasis = [0,1,2,4] # old basis was x1,x2,s3,s4 -> s4 leaving and s1 entering gives x1,x2,s1,s3
newPrimalNonbasis = [3,5]

# step size for the dual can be read by comparing yB and dualRatios
lambdaDual = 2/3

# new basis matrix B
newB = A[:,newPrimalBasis]
# dB for the primal can be found using the new basis
dB = np.linalg.solve(newB,-A[:,leavingPrimal])

# updates!
xFull[leavingPrimal] = 0 # leaving primal variable leaves (goes to zero)
xFull[newPrimalBasis] = xFull[newPrimalBasis] + dB * lambdaPrimal # new primal basis variables get updated

yFull[leavingPrimal] = lambdaDual # entering dual variable enters!
yFull[primalNonbasis] = yFull[primalNonbasis] + dBhat * lambdaDual # dual basis variables get updated (simplex step)

# print all results:
print("lambdaDual:",lambdaDual)
print("dBhat:",dBhat)

print("lambdaPrimal:",lambdaPrimal)
print("dB:",dB)

print("x:",xFull)
print("y:",yFull)