import numpy as np

# Objective function
def objective_function(x):
    return -(x - 2)**2 + 3

# CEM parameters
population_size = 50
elite_frac = 0.2
n_iterations = 100
mean = 0
std_dev = 1

# CEM algorithm
for _ in range(n_iterations):
    # Sample solutions
    samples = np.random.normal(mean, std_dev, population_size)

    # Evaluate objective function
    scores = np.array([objective_function(x) for x in samples])

    # Select the top solutions
    top_indices = np.argsort(-scores)[:int(elite_frac * population_size)]
    top_samples = samples[top_indices]

    # Update distribution parameters
    mean = np.mean(top_samples)
    std_dev = np.std(top_samples)

# Output
print(f"Optimal x: {mean:.2f}, Max value: {objective_function(mean):.2f}")
