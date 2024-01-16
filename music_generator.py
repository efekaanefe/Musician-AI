from genetic_algorithm import GeneticAlgorithm

# to surprass warning error messages
import logging
logging.getLogger().setLevel(logging.ERROR)


# INPUTS
instrument = "piano merlin" 
instrument = "music box" 
instrument = input("Instrument? [piano, guitar, violin, brass]: ")
duration = float(input("Duration for a note in seconds: i.e. [0.75]: ")) # [s] per note 
number_of_notes = int(input("Number of notes to be played: i.e. [8]: "))
pitch_min = int(input("Minimum value of pitch, [C3=70 and C4=82]: "))
pitch_max =  int(input("Maximum value of pitch: "))


# TODO: if this is odd, when generating  popoulation size drops 1, 
#could be done by only adding one genome in loop
population_size = int(input("Population size: "))


mutations_per_genome = int(input("Mutations per genome i.e. [4]: ")) # number of mutations per gnome
mutation_probability = float(input("Mutation probability i.e. [0.5]: ")) # probability for mutation to occur

#num_iters = 5

genetic_algo = GeneticAlgorithm(instrument, 
                                duration,
                                number_of_notes,
                                pitch_min,
                                pitch_max,
                                population_size,
                                mutations_per_genome,
                                mutation_probability)

# run genetic algorithm
population = genetic_algo.generate_population()

#for _ in range(num_iters):,
while True:
    scores = genetic_algo.evaluate_scores(population)
    sorted_population, sorted_scores = genetic_algo.sort_population(population, scores)

    next_generation = list(sorted_population[0:2]) 
    for j in range(population_size // 2 - 1):
        parents = genetic_algo.select_pair(sorted_population, sorted_scores)
        offspring_a, offspring_b = genetic_algo.crossover(parents[0], parents[1])
        offspring_a = genetic_algo.mutation(offspring_a)
        offspring_b = genetic_algo.mutation(offspring_b)
        next_generation += [offspring_a, offspring_b]
    population = next_generation

    scores = genetic_algo.evaluate_scores(population)
    sorted_population, sorted_scores = genetic_algo.sort_population(population, scores)


    print("Here is the best melody: ")
    print(sorted_population[0])
    print("Here is the second best melody: ")
    print(sorted_population[1])

    if input("Want to save them? [Y/n]: ").lower() == "y":
        genetic_algo.save_genome(sorted_population[0])
        genetic_algo.save_genome(sorted_population[1])

    if input("Continue? [Y/n]: ").lower() == "n":   
        break
