# guess password problem - 2024-11-13

import random as rand
import numpy as np

POPULATION_SIZE = 500
TARGET = "hello ga"
MUTATION_RATE = 0.1

GENES = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

def init_population(pop_size, genome_size):
	return ["".join(rand.choices(GENES, k=genome_size)) for _ in range(pop_size)]

def fitness_calc(individual):
	fitness = 0
	for i, j in zip(individual, TARGET):
		if i == j:
			fitness += 1
	return fitness

def selection(population, fitnesses):
	tournament = rand.sample(range(len(population)), k=5)
	tournament_fitness = [fitnesses[i] for i in tournament]
	winner_index = tournament[np.argmax(tournament_fitness)]
	return population[winner_index]

def mutate(individual):
	individual = list(individual)
	for i in range(len(individual)):
		if rand.random() < MUTATION_RATE:
			individual[i] = rand.choice(GENES)
	return ''.join(individual)


def crossover(parent1, parent2):
	xo_point = rand.randint(1, len(parent1) - 1)
	return ([parent1[:xo_point]+parent2[xo_point:], parent2[:xo_point]+parent1[xo_point:]])


def main():
	population = init_population(POPULATION_SIZE, len(TARGET))
	generation_index = 0
	while True:
		population_fitness = [fitness_calc(individual) for individual in population]
		best = population[population_fitness.index(max(population_fitness))]
		print(f"Generation {generation_index}: Best so far = '{best}' with fitness = {max(population_fitness)}")
		if max(population_fitness) == len(TARGET):
			best = population[population_fitness.index(max(population_fitness))]
			print("The password is", best)
			break
		nextgen_population = []
		for i in range(int(POPULATION_SIZE / 2)):
			parent1 = selection(population, population_fitness)
			parent2 = selection(population, population_fitness)
			offspring1, offspring2 = crossover(parent1, parent2)
			nextgen_population += [mutate(offspring1), mutate(offspring2)]
		population = nextgen_population
		generation_index += 1
 
if __name__ == "__main__":
	main()