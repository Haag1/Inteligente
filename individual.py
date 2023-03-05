

class Individual:
    name_ = ""
    id_number_ = ""
    fitness_ = 0

    def __init__(self, name, id_number):
        self.name_ = name
        self.id_number_ = id_number
        self.fitness_ = 0

    # set values for individual
    def set_fitness(self, reference):
        same_character_placement = 0
        individual_full_id = self.get_full_id()
        length_of_individual = len(individual_full_id)
        length_of_reference = len(reference)

        if length_of_reference != length_of_individual:
            print("individual not formatted to dataset")
        else:
            for i in range(length_of_individual):
                if individual_full_id[i] == reference[i]:
                    same_character_placement = same_character_placement + 1

        self.fitness_ = same_character_placement / length_of_individual

    def edit_char_in_full_name(self, index_name, index_id, char, char_id):
        list_of_letters = list(self.name_)
        list_of_numbers = list(self.id_number_)
        list_of_letters[index_name] = char
        list_of_numbers[index_id] = char_id
        self.name_ = "".join(list_of_letters)
        self.id_number_ = "".join(list_of_numbers)

    # get values for individual
    def get_full_id(self):
        return self.name_ + self.id_number_

    def get_name(self):
        return self.name_

    def get_id_number(self):
        return self.id_number_

    def get_fitness(self):
        return self.fitness_
