from random import choice, choices, randint, random
from scamp import *


class GeneticAlgorithm:
    def __init__(self, 
                 instrument, 
                 duration, 
                 number_of_notes, 
                 pitch_min, 
                 pitch_max, 
                 population_size, 
                 mutations_per_genome, 
                 mutation_probability
                ):
        
        self.instrument = instrument
        self.duration = duration
        self.number_of_notes = number_of_notes
        self.pitch_min = pitch_min
        self.pitch_max = pitch_max
        self.population_size = population_size
        self.mutations_per_genome = mutations_per_genome
        self.mutation_probability = mutation_probability

        self.total_duration = self.duration*self.number_of_notes

        # scamp parameters
        self.session = Session()
        #self.session.set_tempo_target(duration_units="beats")
        self.session.tempo = 100
        self.session.synchronization_policy = "no synchronization"
        self.player_instrument = self.session.new_part(self.instrument)
        

    def generate_genome(self):
        return [randint(self.pitch_min, self.pitch_max) for _ in range(self.number_of_notes)]
    
    def generate_population(self):
        return [self.generate_genome() for _ in range(self.population_size)]

    # crossover two parent genomes to create two children
    def crossover(self, p1, p2): # single point crossover
        if len(p1) == len(p2):            
            length = len(p1)
            ci = randint(1, length-1) # crossover index
            return (p1[0:ci] + p2[ci:], p2[0:ci]+p1[ci:])
        else:
            print("parent genomes must be of the same size")

    def mutation(self, genome): 
        genome_copy = genome.copy()
        for _ in range(self.mutations_per_genome):
            if random() > self.mutation_probability:
                index = randint(0,len(genome)-1)
                mutation_multiplier = choice([-1,1])
                mutation_amount = 1
                genome_copy[index] = genome_copy[index] + mutation_multiplier*mutation_amount
        return genome_copy

    def evaluate_scores(self, population):
        scores = []
        for genome in population:
            print("Playing the genome...")
            for note in genome:
                self.player_instrument.play_note(note, 0.8, self.duration)
            point = int(input("What's your rating? [0,5]: "))
            #scores.append(randint(0,5))
            scores.append(point)
        return scores

    def sort_population(self, population, scores):
        sorted_data = sorted(zip(population, scores), key=lambda x: x[1], reverse = True)
        sorted_population, sorted_scores = zip(*sorted_data)
        return sorted_population, sorted_scores

    def select_pair(self, population, scores): 
        return choices(population, weights=scores, k = 2)

    """Saving is possible via using "MuseScore 3" app, 
       which opens the melody as a musical sheet??,
       from there you can save it as a MIDI file.
       However, this is a pretty long process 
       compared to saving directly from code."""
    def save_genome(self, genome): 
        pass
