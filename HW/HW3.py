print("Problem 1:")
# a) L2-Norm
import numpy as np
import cvxpy as cp

power_consumed = np.array([10, 8, 13, 15, 9])
distance = np.array([60, 55, 75, 81, 62])
m1, b1 = np.polyfit(power_consumed, distance, 1)
print(f"(a): m1 = {m1:.2f}, b1 = {b1:.2f}")

# b) L1-Norm
m2 = cp.Variable()
b2 = cp.Variable()
diff = cp.abs(distance - m2*power_consumed - b2)
obj_1b = cp.Minimize(cp.sum(diff))
prob_1b = cp.Problem(obj_1b)
prob_1b.solve()
m2 = m2.value
b2 = b2.value
print(f"(b): m2 = {m2:.2f}, b2 = {b2:.2f}")

# c) Infinity-Norm
m3 = cp.Variable()
b3 = cp.Variable()
error = cp.Variable()
constraints_1c = [cp.abs(distance - m3*power_consumed - b3) <= error]
obj_1c = cp.Minimize(error)
prob_1c = cp.Problem(obj_1c, constraints_1c)
prob_1c.solve()
m3 = m3.value
b3 = b3.value
print(f"(c): m3 = {m3:.2f}, b3 = {b3:.2f}")

# d) plot
import matplotlib.pyplot as plt

plt.scatter(power_consumed, distance, label="Data")
plt.plot(power_consumed, m1*power_consumed + b1, label=f"Least Squares (L2): D = {m1:.2f}P + {b1:.2f}")
plt.plot(power_consumed, m2*power_consumed + b2, label=f"L1-Norm: D = {m2:.2f}P + {b2:.2f}")
plt.plot(power_consumed, m3*power_consumed + b3, label=f"Infinity Norm: D = {m3:.2f}P + {b3:.2f}")
plt.legend()
plt.xlabel("Power Consumed")
plt.ylabel("Distance")
plt.show()
###################################################################
print(" ")
print("Problem 2: See in doc.")
###################################################################
print(" ")
print("Problem 3:")
run_time = ["A", "B", "C"]
process = [[9, 5, 50, 9, 6],
           [6, 8, 75, 12, 4],
           [4, 11, 100, 10, 6]]
Availability = [200, 400, 1850]

chemical_produced = cp.Variable(len(run_time))

obj_3 = cp.Maximize(15*chemical_produced[0] + 16*chemical_produced[1] + 16*chemical_produced[2])

totalMaterial_1 = cp.sum([process[i][0]*chemical_produced[i] for i in range(len(run_time))])
totalMaterial_2 = cp.sum([process[i][1]*chemical_produced[i] for i in range(len(run_time))])
totalFuel = cp.sum([process[i][2]*chemical_produced[i] for i in range(len(run_time))])
totalChemical_1 = cp.sum([process[i][3]*chemical_produced[i] for i in range(len(run_time))])
totalChemical_2 = cp.sum([process[i][4]*chemical_produced[i] for i in range(len(run_time))])

constraints_3 = [totalMaterial_1 <= Availability[0],
                 totalMaterial_2 <= Availability[1],
                 totalFuel <= Availability[2],
                 totalChemical_1 - 2.5*totalChemical_2 == 0]
for i in range(len(run_time)):
    constraints_3.append(chemical_produced[i] >= 0)

prob_3 = cp.Problem(obj_3, constraints_3)
result_3 = prob_3.solve()
A = chemical_produced[0].value
B = chemical_produced[1].value
C = chemical_produced[2].value

print(f"Optimal total amount of blend manufactured: {result_3:.2f}")
print(f"Times to run A: {A:.2f}")
print(f"Times to run B: {B:.2f}")
print(f"Times to run C: {C}")
##############################################################
print(" ")
print("Problem 4:")
Alloy = ["Alloy 1", "Alloy 2", "Alloy 3", "Alloy 4", "Alloy 5"]
cost = [19, 17, 23, 21, 25]
tin_percent = [0.6, 0.25, 0.45, 0.2, 0.5]
zinc_percent = [0.1, 0.15, 0.45, 0.5, 0.4]
lead_percent = [0.3, 0.6, 0.1, 0.3, 0.1]
alloy_proportion = [0.4, 0.35, 0.25]
total_produced = 1

newAlloy = cp.Variable(len(Alloy), pos=True)
production = cp.Minimize(cp.sum([cost[i]*newAlloy[i] for i in range(len(Alloy))]))

total = cp.sum([newAlloy[i] for i in range(len(Alloy))])
total_tin = cp.sum([tin_percent[i]*newAlloy[i] for i in range(len(Alloy))])
total_zinc = cp.sum([zinc_percent[i]*newAlloy[i] for i in range(len(Alloy))])
total_lead = cp.sum([lead_percent[i]*newAlloy[i] for i in range(len(Alloy))])

constraints_4 = [total_tin == alloy_proportion[0]*total,
                total_zinc == alloy_proportion[1]*total,
                total_lead == alloy_proportion[2]*total,
                 total == total_produced]
for i in range(len(Alloy)):
    constraints_4.append(newAlloy[i] >= 0)

prob_4 = cp.Problem(production, constraints_4)
result_4 = prob_4.solve()

print(f"Proportion of each alloy for producing {total_produced} new Alloy:")
print(f"Alloy 1 = {newAlloy[0].value:.2f}")
print(f"Alloy 2 = {newAlloy[1].value}")
print(f"Alloy 3 = {newAlloy[2].value:.2f}")
print(f"Alloy 4 = {newAlloy[3].value:.2f}")
print(f"Alloy 5 = {newAlloy[4].value}")
print(f"Minimum cost is ${result_4:.2f}")
##########################################################
print(" ")
print("Problem 5: see in doc.")






