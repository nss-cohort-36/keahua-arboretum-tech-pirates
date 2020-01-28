import sys
sys.path.append('../')

from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from interfaces.animals.aquatic import IsAquatic
from interfaces.animals.terrestrial import IsTerrestrial  

class Forest(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self, name="Forest", max_plants=32, max_animals=20):
        self.name = name
        self.max_plants = max_plants
        self.max_animals = max_animals
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)

    def add_animal(self, animal):
        super().animals.append(animal)

    def add_plant(self, plant):
        super().plants.append(plant)