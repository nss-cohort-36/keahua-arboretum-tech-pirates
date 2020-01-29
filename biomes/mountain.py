from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from interfaces import Identifiable

class Mountain(IContainsAnimals, IContainsPlants, Identifiable):
    
    def __init__(self):
        self.name = "Mountain"
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_plant(self, plant):
        self.plants.append(plant)

    def __str__(self):
        return f'Mountain.'

  
