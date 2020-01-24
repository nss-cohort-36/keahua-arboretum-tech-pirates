from interfaces.animals.terrestrial import IsTerrestrial
from interfaces.habitat.contains_animals import IContainsAnimals
from interfaces.habitat.contains_plants import IContainsPlants
from interfaces.identifiable import Identifiable

# Import interfaces that support this class

class Grassland(IContainsAnimals, IContainsPlants, Identifiable):
    
    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        
    def add_animal(self, animal):
        pass
    
    def add_plant(self, plant):
        