import itertools

# Sample data: Distances between cities
distances = {
    (0, 1): 10, (0, 2): 15, (0, 3): 20,
    (1, 0): 10, (1, 2): 35, (1, 3): 25,
    (2, 0): 15, (2, 1): 35, (2, 3): 30,
    (3, 0): 20, (3, 1): 25, (3, 2): 30
}
cities = [0, 1, 2, 3]

def calculate_route_distance(route):
    return sum(distances[(route[i], route[i+1])] for i in range(len(route)-1))

# Brute force for simplicity
min_distance = float('inf')
min_route = None
for route in itertools.permutations(cities):
    current_distance = calculate_route_distance(route + (route[0],))
    if current_distance < min_distance:
        min_distance = current_distance
        min_route = route

print("Shortest Route:", min_route)
print("Distance:", min_distance)

def solve_tsp(distances, num_cities, num_iterations=100, sample_size=1000):
    # Generate all possible routes (permutations)
    routes = list(itertools.permutations(range(num_cities)))
    
    for _ in range(num_iterations):
        # Sample routes based on uniform probability
        sampled_routes = np.random.choice(len(routes), size=sample_size)
        
        # Evaluate each route
        route_distances = [sum(distances[routes[i][j-1], routes[i][j]] for j in range(num_cities)) for i in sampled_routes]
        
        # Select the shortest route
        min_distance_idx = np.argmin(route_distances)
        best_route = routes[sampled_routes[min_distance_idx]]

        # For simplicity, the distribution is not updated in this implementation
        # In a complete CE implementation, the distribution would be updated to favor shorter routes

    return best_route, route_distances[min_distance_idx]

# Example usage
distances = {(i, j): np.random.uniform(1, 100) for i in range(5) for j in range(5) if i != j}  # Random distances
best_route, best_distance = solve_tsp(distances, num_cities=5)
print("Best Route:", best_route)
print("Total Distance:", best_distance)
