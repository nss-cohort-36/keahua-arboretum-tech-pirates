from interfaces.habitats import IContainsAnimals, IContainsPlants
from interfaces import Identifiable

class Mountain(IContainsAnimals, IContainsPlants, Identifiable):
    
    def __init__(self, name):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.name = name
    
    def __str__(self):
        return f'{self.name} Mountain.'

  