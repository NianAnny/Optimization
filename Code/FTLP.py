import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

# Given the solutions P = {(1, 2), (4, 3), (5, 7), (0, 7)}, what linear inequalities
# describe the convex hull of P? What are its extreme points?

points = np.array([(1, 2), (4, 3), (5, 7), (0, 7)])

# Determine the convex hull
hull = ConvexHull(points)

# Plot the convex hull
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

plt.show()

# Print the extreme points
print("Extreme Points of the Convex Hull:")
for vertex in hull.vertices:
    print(points[vertex])

# To get the inequalities, we can use the equations attribute of hull
print("\nLinear Inequalities (in the form Ax + By + C <= 0):")
for eq in hull.equations:
    print(f"{eq[0]:.2f}x + {eq[1]:.2f}y + {eq[2]:.2f} <= 0")
