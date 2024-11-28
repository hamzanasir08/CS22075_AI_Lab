import random
# Genetic Algorithm Parameters
POPULATION_SIZE = 100
GENERATIONS = 100
MUTATION_RATE = 0.1
MUTATION_AMOUNT = 1

# Get items and max weight from the user
def get_user_input():
    num_items = int(input("Enter the number of items: "))
    items = []
    
    for i in range(num_items):
        print(f"\nItem {i + 1}:")
        weight = int(input("  Enter weight: "))
        value = int(input("  Enter value: "))
        items.append((weight, value))
        
    max_weight = int(input("\nEnter the maximum weight the knapsack can carry: "))
    
    # Display all items in a table-like format
    print("\n")
    print(50*"=")
    print("\t\t  Items Summary")
    print(50*"=")
    print("\t{:<10} \t{:<10} \t{:<10}".format("Item No.", "Weight", "Value"))
    print("-" * 50)
    for i, (weight, value) in enumerate(items, start=1):
        print("\t{:<10} \t{:<10} \t{:<10}".format(i, weight, value))
    
    print(f"\nMaximum knapsack weight capacity: {max_weight}\n")
    return items, max_weight



# Fitness function
def fitness(individual, items, max_weight):
    total_value = 0
    total_weight = 0
    
    for i in range(len(items)):
        if individual[i] == 1:
            total_value += items[i][1]
            total_weight += items[i][0]
    
    if total_weight > max_weight:
        return 0  # Penalize invalid solutions (exceeds weight limit)
    else:
        return total_value


# Selection function
def selection(population, items, max_weight):
    weights = []
    for ind in population:
        weights.append(fitness(ind, items, max_weight))
    return random.choices(population, weights=weights, k=2)


# Crossover function (One-point crossover)
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutation function
def mutate(individual):
    if random.random() < MUTATION_RATE:
        index = random.randint(0, len(individual) - 1)
        individual[index] = 1 - individual[index]  # Flip the bit (0 -> 1, 1 -> 0)
    return individual

# Initialize population
def create_population(size, chromosome_length):
    return [[random.randint(0, 1) for _ in range(chromosome_length)] for _ in range(size)]

# Main Genetic Algorithm loop
def genetic_algorithm(items, max_weight):
    CHROMOSOME_LENGTH = len(items)
    population = create_population(POPULATION_SIZE, CHROMOSOME_LENGTH)
    
    best_solution = None  # Variable to store the best solution found
    best_fitness = -1  # Initialize best fitness to a low value
    
    for generation in range(GENERATIONS):
        # Selection
        parent1, parent2 = selection(population, items, max_weight)
        
        # Crossover
        child1, child2 = crossover(parent1, parent2)
        
        # Mutation
        mutate(child1)
        mutate(child2)
        
        # Add children to population
        population.append(child1)
        population.append(child2)
        
        # Sort population by fitness and keep top individuals
        population = sorted(population, key=lambda ind: fitness(ind, items, max_weight), reverse=True)
        population = population[:POPULATION_SIZE]
        
        # Print best solution of the generation
        best_individual = population[0]
        current_fitness = fitness(best_individual, items, max_weight)
        
        # If current best solution is better, update best_solution
        if current_fitness > best_fitness:
            best_fitness = current_fitness
            best_solution = best_individual
        
        # Check if solution is good enough (fitness close to max value)
        if current_fitness == sum(item[1] for item in items):
            print("Optimal solution found!")
            break

    # After all generations, print the best overall solution
    # print(f"\nBest Solution after all generations: {best_solution}, Fitness = {best_fitness}"
    # for res in range(len(best_solution)):
    #     if best_solution[res] == 1:
    #         print(items[res], "should be included")
    #     else:
    #         print(items[res], "should not be included")
    print("\n")
    print(70 * "=")
    print("\t\t\tKnapsack Solution Summary")
    print(70 * "=")
    print("\t{:<10} \t{:<10} \t{:<10} \t{:<10}".format("Item No.", "Weight", "Value", "Included"))
    print("-" * 70)
    
    for i, (weight, value) in enumerate(items, start=1):
        inclusion = "Yes" if best_solution[i - 1] == 1 else "No"
        print("\t{:<10} \t{:<10} \t{:<10} \t{:<10}".format(i, weight, value, inclusion))



print(50*"=")
print("\t\tKnapsack Problem")
print(50*"=")
# Get user input and run the genetic algorithm
items, max_weight = get_user_input()
genetic_algorithm(items, max_weight)
