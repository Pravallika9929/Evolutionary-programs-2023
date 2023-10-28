import random
population_size = 100 # Size of the population generations = 50 # Number of generations mutation_rate = 0.1 # Probability of mutation knapsack capacity = 10 * 50 Capacity of the knapsack
population = [[random.randint ( theta .1) for in range(len(items))] for in range(population_size)]
total_value = sum(items[i][0] for i in range(len(solution)) if solution [i] = 1 ) total weight sum(items[i][1] for i in range(len(solution)) if solution[i] == 1 )
if total weight knapsack_capacity:
return 0
else:
return total_value
fitness_scores = [fitness (individual) for individual in population]
parents = 0
for in range(population size // 2):
parent1 = random.choices (population, weights fitness_scores)[0] parent2 = random.choices (population, weights fitness_scores)[0] parents.append((parent1, parent2))
# Create a new generation through crossover and mutation
new_population 0 for parent1, parent? in parents:
crossover_point = random.randint(1, len(items) 1) child parent1[:crossover_point] + parent2[crossover_point:]
Apply mutation
for i in range(len(child)): if random.random() mutation_rate: child[i] 1- child[i]
new_population.append(child)
population = new_population
Find the best solution in the final population
best solution = max(population, key=fitness)
best_value = sum(items[i][0] for i in range(len(best solution)) if best solution [i] ==1)
best_weight=sum(items[i][1] for i in range(len(best solution)) if best solution [1] ==1 )
print("Best solution:", best solution) print("Total value:", best_value) print("Total weight:", best weight)
