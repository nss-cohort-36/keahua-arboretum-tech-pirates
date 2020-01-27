from arboretum import Arboretum
from interfaces.animals.aquatic import IsAquatic
from interfaces.identifiable import Identifiable
from interfaces.habitat.contains_animals import IContainsAnimals
from interfaces.habitat.contains_plants import IContainsPlants

class Coastline(Arboretum, Identifiable, IContainsAnimals, IContainsPlants):

    def __init__(self):
        Identifiable.__init__(self)
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypotonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or freshwater animals to a coastline")
