import random

# Parameters
POPULATION_SIZE = 20
GENES = '01'  # Binary representation
CHROMOSOME_LENGTH = 10
MUTATION_RATE = 0.01
GENERATIONS = 50

# Fitness function: example - maximize the number of 1's
def fitness(chromosome):
    return chromosome.count('1')

# Create a random chromosome
def create_chromosome():
    return ''.join(random.choice(GENES) for _ in range(CHROMOSOME_LENGTH))

# Create initial population
def create_population():
    return [create_chromosome() for _ in range(POPULATION_SIZE)]

# Selection: Tournament selection
def selection(population):
    tournament_size = 3
    selected = random.sample(population, tournament_size)
    return max(selected, key=fitness)

# Crossover: Single-point crossover
def crossover(parent1, parent2):
    if random.random() < 0.7:  # Crossover probability
        point = random.randint(1, CHROMOSOME_LENGTH - 1)
        return parent1[:point] + parent2[point:]
    return parent1

# Mutation: Flip a random bit
def mutate(chromosome):
    chromosome = list(chromosome)
    for i in range(CHROMOSOME_LENGTH):
        if random.random() < MUTATION_RATE:
            chromosome[i] = '1' if chromosome[i] == '0' else '0'
    return ''.join(chromosome)

# Genetic Algorithm main loop
def genetic_algorithm():
    population = create_population()

    for generation in range(GENERATIONS):
        print(f"Generation {generation}, Best Fitness: {max(fitness(ch) for ch in population)}")

        # Create new generation
        new_population = []
        for _ in range(POPULATION_SIZE // 2):  # Create pairs
            parent1 = selection(population)
            parent2 = selection(population)
            offspring1 = crossover(parent1, parent2)
            offspring2 = crossover(parent2, parent1)
            new_population.append(mutate(offspring1))
            new_population.append(mutate(offspring2))

        population = new_population

    # Final result
    best_solution = max(population, key=fitness)
    print(f"Best solution: {best_solution}, Fitness: {fitness(best_solution)}")

# Run the genetic algorithm
if __name__ == "__main__":
    genetic_algorithm() 