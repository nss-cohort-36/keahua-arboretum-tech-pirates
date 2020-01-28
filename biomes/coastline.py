from arboretum import Arboretum
from interfaces.animals.aquatic import IsAquatic
from interfaces.identifiable import Identifiable
from interfaces.habitats.contains_animals import IContainsAnimals
from interfaces.habitats.contains_plants import IContainsPlants

class Coastline(Arboretum, Identifiable, IContainsAnimals, IContainsPlants):

    def __init__(self):
        Identifiable.__init__(self)
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)

    def add_animal(self):
        super().animals.append(animal)

    def add_plant(self, plant):
        super().plants.append(plant)