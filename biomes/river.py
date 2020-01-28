#********************************************************************************************************************
# This file defines the River class  
#********************************************************************************************************************

from interfaces import IsAquatic
from interfaces import Identifiable
from interfaces.habitats.contains_animals import IContainsAnimals
from interfaces import IContainsPlants
# from animals import RiverDolphin


class River(IContainsAnimals, IContainsPlants, Identifiable): # <-- creates def of River class which is a derivitive class of 3 parent classes

    def __init__(self): # the 3 lines below give River access to the __init__'s in the parent files
        self.name = "River"
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.max_animals = 12
        self.max_plants = 6

    def add_animal(self, animal): # <-- this is a function that can be executed once a River class has been instantiated
        try:
            if animal.aquatic and animal.cell_type == "hypotonic":
                super().animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")
# Missing Logic for conditonals to complete functionality noice
    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                super().plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river biome")
