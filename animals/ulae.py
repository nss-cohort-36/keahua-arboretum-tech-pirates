from interfaces.animals import IsSaltwater
from animals import Animal
from interfaces import Identifiable

class Ulae(Animal, IsSaltwater, Identifiable):
    def __init__(self):
        Animal.__init__(self, "Ulae")
        IsSaltwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Fish" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The ulae ate {prey} for a meal')
        else:
            print(f'The ulae rejects the {prey}')
    
    def __str__(self):
        return f'Ulae {self.id}.'

    