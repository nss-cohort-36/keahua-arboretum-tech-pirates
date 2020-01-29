import sys
sys.path.append('../')
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants

class Grassland(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self, name="Grassland", max_animals=22, max_plants=15):
        self.name = name
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.max_plants = max_plants
        self.max_animals = max_animals
        
    def add_animal(self, animal):
        self.animals.append(animal)
        
    def add_plant(self, plant):
        self.plants.append(plant)