# import sys
# sys.path.append('../')
<<<<<<< HEAD
from interfaces.habitats import IsStagnant
=======
# from interfaces.habitats import IsStagnant
>>>>>>> master
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
# from animals.

# from environments.environment import Environment


class Swamp(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self, name):
        self.name = name
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)

    def animal_count(self):
        return "This place has a bunch of animals in it"
    
    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypotonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic or saltwater animals to a swamp")

    def add_plant(self, plant):
        try:
<<<<<<< HEAD
            if plant.freshwater and plant.is_stagnant:
=======
            if plant.freshwater :
            # and plant.is_stagnant 
>>>>>>> master
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require brackish water or currents to a swamp biome")

    # def __str__(self):
    #     return self.name
