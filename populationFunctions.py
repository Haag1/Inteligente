from individual import *


# functions to manipulate the population
# -----------------------------------------------------------------------
def calculate_population_fitness(population, reference):
    array_length = len(population)

    for i in range(array_length):
        population[i].set_fitness(reference)

    return population


def four_point_split(parent_name, parent_id_number, cut_off_point_1, cut_off_point_2):
    parts = []
    parts.append(parent_name[:cut_off_point_1])
    parts.append(parent_name[cut_off_point_1:])

    parts.append(parent_id_number[:cut_off_point_2])
    parts.append(parent_id_number[cut_off_point_2:])
    return parts
# -----------------------------------------------------------------------
