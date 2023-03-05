from populateFunctions import *
from individual import *
from populationFunctions import *
import random

# components for target string
targetName = "hagen" + "ostgard"
targetStudentID = "123456"

# target identification is based on name surname and id-number
targetId = targetName + targetStudentID

# parameters for GA
populationSize = 10
stringLength = len(targetId)
crossoverProbability = 0.6
mutationProbability = 0.05
maxGenerations = 5000

# the starting population
population = create_population(10)

# calculate fitness for whole population
population = calculate_population_fitness(population, targetId)

# sort population based on fitness
population.sort(key=lambda individual: individual.get_fitness(), reverse=True)

# evolution loop
numberOfCrossovers = round(crossoverProbability * populationSize / 2)
numberOfMutatedValues = round(mutationProbability * stringLength * populationSize)

# defines cutoff points for name and id-number
cutOfPointName = round(len(targetName) / 2)
cutOfPointIdNumber = round(len(targetStudentID) / 2)

generations = []

for generation in range(maxGenerations):

    # empty vector for children, to reset between generations
    children = []

    for crossover in range(numberOfCrossovers):
        # select two parents from first and second half of population
        parent1 = population[random.randint(0, round(populationSize / 4))]
        parent2 = population[random.randint(round(populationSize / 4) + 1, round(populationSize / 2))]

        # store the parts after split in separate arrays
        parent1parts = four_point_split(parent1.get_name(), parent1.get_id_number(), cutOfPointName, cutOfPointIdNumber)
        parent2parts = four_point_split(parent2.get_name(), parent2.get_id_number(), cutOfPointName, cutOfPointIdNumber)

        # give attributes from parents to children
        child1 = Individual(parent1parts[0] + parent2parts[1], parent1parts[2] + parent2parts[3])
        child2 = Individual(parent2parts[0] + parent1parts[1], parent2parts[2] + parent1parts[3])

        children.append(child1)
        children.append(child2)

    for gene in range(numberOfMutatedValues):
        children[gene % len(children)].edit_char_in_full_name(random.randint(0, 11),
                                                              random.randint(0, 5),
                                                              random.choice(string.ascii_lowercase),
                                                              str(random.randint(0, 9)))

    children = calculate_population_fitness(children, targetId)

    for i in range(len(children)):
        population[populationSize - 1 - i] = children[i]

    population = calculate_population_fitness(population, targetId)
    population.sort(key=lambda individual: individual.get_fitness(), reverse=True)

    generations.append(population[0])

    print(str(generation) + " " + str(generations[generation].get_fitness()) + " " + generations[generation].get_full_id())

for i in range(10):
    print(generations[maxGenerations - i - 1].get_full_id())


print("")
print(generations[maxGenerations-1].get_full_id() + " " + str(generations[maxGenerations-1].get_fitness()))
print(targetId)
