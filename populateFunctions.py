import string
import random
from individual import *


# generate a new population
# -------------------------------------------------------------------------
# from https://pynative.com/python-generate-random-string/
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def get_random_int(length):
    total_integer_string = ""

    for i in range(length):
        total_integer_string = total_integer_string + str(random.randint(0, 9))

    return total_integer_string


def create_population(size):
    population = []
    for i in range(size):
        population.append(Individual(get_random_string(12), get_random_int(6)))
    return population
# -------------------------------------------------------------------------
