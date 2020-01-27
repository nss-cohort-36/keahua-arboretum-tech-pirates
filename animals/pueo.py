from interfaces.animals import IsTerrestrial
from interfaces import IsFlying 
from animals import Animal
from interfaces import Identifiable

class Pueo(Animal, IsTerrestrial, IsFlying, Identifiable):
    def __init__(self):
        Animal.__init__(self, "Pueo")
        IsTerrestrial.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Rodents" }

    @property
    def prey(self):
        return self.__prey
    
    def feed(self, prey):
        if prey in self.__prey:
            print(f'The pueo ate {prey} for a meal')
        else:
            print(f'The pueo rejects the {prey}')
    
    def __str__(self):
        return f'Pueo {self.id}.'