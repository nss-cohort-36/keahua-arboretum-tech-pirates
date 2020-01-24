from interfaces.habitats import IContainsAnimals
from interfaces.habitats import IContainsPlants
from interfaces import Identifiable

class Mountain(IContainsAnimals, IContainsPlants, Identifiable):
    def __init__(self):
        