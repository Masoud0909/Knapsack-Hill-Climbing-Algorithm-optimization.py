capacity = 5  # capacity of the knapsack, the maximum weight the knapsack can hold


# Function for the weights and values of the items that can be placed in the knapsack
def weight_values():
    weights = [2, 3, 4, 5]  # weights of the items
    values = [3, 4, 5, 8]  # corresponding value of each item
    return weights, values


import random


# Generate a random initial solution (list of 1s and 0s)
def initialize_solution(num_items):  # make a list of 1/0 with n=num_items
    # randomly creates a list of 1s and 0s for num_items, representing the inclusion (1) or exclusion (0) of each item
    return [random.randint(0, 1) for i in range(num_items)]


weights, values = weight_values()
selection = initialize_solution(len(weights))
print(f"weights and values are: {weights, values}")
print(f"initial solution is {selection}")


def evaluate_solution(weights, values, selection):
    sumweight = 0
    sumvalue = 0
    # here it clculates the total weight and value of the current solution based on the selected items
    for i in range(len(selection)):
        if selection[i] == 1:  # if selected
            sumweight += weights[i]
            sumvalue += values[i]
    return sumweight, sumvalue  # return both the total weight and value of the selected solution


sum_of_current_weight, sum_of_current_value = evaluate_solution(weights, values, selection)
print(f"Total weight: {sum_of_current_weight}, total value: {sum_of_current_value}")


def generate_neighbours(selection):
    # this function Generates all possible neighbors by flipping one item at a time in the solution
    neighbors = []
    for i in range(len(selection)):
        neighbor = selection[:]
        neighbor[i] = 1 - neighbor[i]  # Flip the bit at index i (1 becomes 0, and 0 becomes 1)
        neighbors.append(neighbor)  # add the modified solution to the list of neighbors
    return neighbors


def hill_climbing(weights, values, capacity, max_iterations=100, max_restart=100):
    # Hill climbing algorithm with random restarts to escape local optima
    best_solution = None
    best_weight = 0
    best_value = 0
    for restart in range(max_restart):  # allows multiple restarts for not getting stuck in local optima
        current_solution = initialize_solution(len(weights))  # Generate a new random solution at each restart
        new_sum_weights, new_sum_values = evaluate_solution(weights, values, current_solution)

        for iteration in range(max_iterations):  # improve iterativelry
            neighbor = generate_neighbours(current_solution)  # Generate all possible neighbors
            neighbor_weights, neighbor_values = evaluate_solution(weights, values, neighbor)

            if neighbor_weights <= capacity and neighbor_values > new_sum_values:
                # If the neighbor solution is better and fits within the capacity, move to it
                current_solution = neighbor
                new_sum_values = neighbor_values
                new_sum_weights = neighbor_weights
        if new_sum_values > best_value and new_sum_weights <= capacity:
            # Update the best solution found so far
            best_solution = current_solution
            best_weight = new_sum_weights
            best_value = new_sum_values

    print(
        f"Restart {restart + 1}: Best Solution found as: {best_solution}, with weight{best_weight} and value of {best_value}")
    return best_solution, best_weight, best_value


def print_solution_details(solution, weights, values):
    # Outputs detailed information about the selected items, their weights, and values (I created this mostly for debugging purposes)
    selected_items = [i for i in range(len(solution)) if solution[i] == 1]
    selected_weights = [weights[i] for i in selected_items]
    selected_values = [values[i] for i in selected_items]

    print(f"Selected items: {selected_items}")
    print(f"Corresponding weights: {selected_weights}")
    print(f"Corresponding values: {selected_values}")
    print(f"Total weight: {sum(selected_weights)}, Total value: {sum(selected_values)}")


def main():
    # testing the whole program
    weight, value = weight_values()
    best_solution, best_weight, best_value = hill_climbing(weight, value, capacity)
    print(
        f"Best solution is: {best_solution}, with the best weight of {best_weight}, and highest value of {best_value} ")
    print_solution_details(best_solution, weights, values)  # for clarification


if __name__ == "__main__":
    main()
