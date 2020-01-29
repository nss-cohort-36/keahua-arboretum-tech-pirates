import sys
sys.path.append('../')
from animals.animal import Animal
from interfaces import Identifiable
from interfaces import IsFlying

class Opeapea(Animal, IsFlying, Identifiable):
    def __init__(self):
        Animal.__init__(self, "Ope'ape'a")
        IsFlying.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Centipedes", "Cockroaches", "Assassin Bug", "Golden Tortoise Beetle", "Dobsonflies", "The Eastern Velvet Ant (Cow-Killer)", "Candlenut", "Pineapple", "Breadfruit", "Edible Canna", "Seagrape", "Papaya", "Coconut" }

    @property
    def prey(self):
        return self.__prey
    
    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Opeapea ate {prey} for a meal')
        else:
            print(f'The Opeapea rejects the {prey}')
    
    def __str__(self):
        return f'Opeapea {self.id}.'



