import sys
sys.path.append('../')
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants

class Grassland(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        
    def add_animal(self, animal):
        self.animals.append(animal)
        
    def add_plant(self, plant):
        self.plants.append(plant)