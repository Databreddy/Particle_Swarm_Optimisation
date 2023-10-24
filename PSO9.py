from pyswarm import pso
import numpy as np

# Define the objective function that you want to maximize (negative because PSO performs minimization)
def objective_function(x):
    return -(x[0]**2 + x[1]**2)+10

# Define the combined constraint function
def constraint_function(x):
    # Constraint 1: x + y >= 1
    constraint1 = max(0, x[0] + x[1] - 1)
    # Constraint 2: x - y <= 2
    constraint2 = max(0, x[0] - x[1] - 2)
    return constraint1 + constraint2  # Combine constraints with penalty

# Define the bounds for each variable
lower_bound = [-10, -10]  # Lower bounds for x and y
upper_bound = [10, 30]  # Upper bounds for x and y

# Use PSO to solve the maximization problem with multiple constraints and 10000 iterations
best_solution, min_value = pso(objective_function, lower_bound, upper_bound, f_ieqcons=constraint_function, maxiter=1000)

# Print the results
print("Best solution: ", best_solution)
print("Minimum value: ", min_value)  # Multiply by -1 to get the actual maximum value
