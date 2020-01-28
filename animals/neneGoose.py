from interfaces.animals import IsTerrestrial
from animals import Animal
from interfaces import Identifiable
from interfaces import IsFlying

class Nene_Goose(Animal, IsFlying, Identifiable):
    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        IsFlying.__init__(self)
        IsTerrestrial.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Candlenut", "Pineapple", "Breadfruit", "Edible Canna", "Seagrape", "Papaya", "Coconut" }

    @property
    def prey(self):
        return self.__prey
    
    def feed(self, prey):
        if prey in self.__prey:
            print(f'The nene goose ate {prey} for a meal')
        else:
            print(f'The nene goose rejects the {prey}')
    
    def __str__(self):
        return f'Nene goose {self.id}.'