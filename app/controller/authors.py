import names
import random

class RandomNameGenerator:
    def __init__(self, num_names=10):
        self.num_names = num_names
    
    def generate_names(self):
        """
        Generate a list of random names using the `names` library.
        """
        name_list = []
        for i in range(self.num_names):
            name = names.get_first_name()
            name_list.append(name)
        return name_list
    
    def generate_unique_names(self):
        """
        Generate a list of unique random names using the `names` library.
        """
        name_set = set()
        while len(name_set) < self.num_names:
            name = names.get_first_name()
            name_set.add(name)
        return list(name_set)
    
    def generate_random_pairs(self):
        """
        Generate a list of random pairs of names using the `names` library.
        """
        name_list = self.generate_names()
        random.shuffle(name_list)
        pairs = []
        for i in range(0, self.num_names, 2):
            pair = (name_list[i], name_list[i+1])
            pairs.append(pair)
        return pairs
