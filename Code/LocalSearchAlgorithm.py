import numpy as np
import time
import matplotlib.pyplot as plt

A = np.array([[3,1,-1],
              [0,5,2],
              [-3,-1,12]])
b = np.array([3,1,-5])

exactSol = np.linalg.solve(A,b)
print(exactSol)
#######################################################################
size = 3000

A = np.random.rand(size,size)
b = np.random.rand(size)

start = time.time()
x = np.linalg.solve(A,b)
end = time.time()
print("Time to solve system of size",size,":",end - start)
#####################################################################
sizes = np.array([2 ** i for i in range(14)])
timeToSolve = np.zeros(len(sizes))

for i in range(len(sizes)):
    size = sizes[i]
    A = np.random.rand(size, size)
    b = np.random.rand(size)
    start = time.time()
    x = np.linalg.solve(A, b)
    end = time.time()
    timeToSolve[i] = end - start

plt.plot(sizes, timeToSolve, '.')
plt.show()
###################################################################
# plt.plot(np.log(sizes),np.log(timeToSolve),'.')
###################################################################
xOld = 1.
yOld = 1.
zOld = 1.

tol = 10 ^ -17
i = 0
sizeChange = tol + 1

while sizeChange > tol:
    i += 1
    xNew = (3 - yOld + zOld) / 3
    yNew = (1 - 2 * zOld) / 5
    # zNew = (-5 + 3*xOld + yOld)/12
    zNew = (-5 + 3 * xOld + yOld) / .1

    change = np.array([xNew - xOld, yNew - yOld, zNew - zOld])
    sizeChange = np.linalg.norm(change)  # finds the length of the vector

    xOld = xNew
    yOld = yNew
    zOld = zNew

    if i > 1000:
        break

print([xNew, yNew, zNew], "Number of iterations:", i)
#####################################################################
A = np.array([[3,1,-1],
              [0,5,2],
              [-3,-1,.1]])
b = np.array([3,1,-5])

exactSol = np.linalg.solve(A,b)
print(exactSol)