import sys
sys.path.append('../')
# from interfaces.habitats import IsStagnant
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from animals.river_dolphin import RiverDolphin


class Swamp(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        self.name = "Swamp"
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.max_animals = 8
        self.max_plants = 12

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
            if plant.freshwater :
            # and plant.is_stagnant 
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require brackish water or currents to a swamp biome")
