from interfaces.animals import IsTerrestrial
from animals import Animal
from interfaces import Identifiable

class Pueo(Animal, IsTerrestrial, Identifiable):
    def __init__(self):
        Animal.__init__(self, "Pueo")
        IsTerrestrial.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Rodent", "Insect", "Bird" }

    @property
    def prey(self):
        return self.__prey