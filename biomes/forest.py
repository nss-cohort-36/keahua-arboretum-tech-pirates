from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from interfaces.animals.aquatic import IsAquatic
from interfaces.animals.terrestrial import IsTerrestrial  

class Forest(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)

    def add_animal(self, animal):
        try:
            if animal is IsTerrestrial and animal.cell_type != "hypertonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add saltwater animals to a forest.")
       
# Missing Logic for conditonals to complete functionality noice
    def add_plant(self, plant):
        # try:
            # Change animal.cell_type to plant.cell_type, but need class for plant
            # if plant.freshwater and animal.cell_type != "hypertonic":
        self.plants.append(plant)
        # except AttributeError:
        #     raise AttributeError("Cannot add saltwater plants to a forest.")
