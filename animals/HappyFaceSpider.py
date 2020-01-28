from animals import Animal
from interfaces import Identifiable
from interfaces import IsTerrestrial

class Hawaiian_Happy_Face_Spider(Animal, IsTerrestrial, Identifiable):
    def __init__(self):
        Animal.__init__(self, "Hawaiian Happy-Face Spider")
        IsTerrestrial.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Centipedes", "Cockroaches", "Assassin Bug", "Golden Tortoise Beetle", "Dobsonflies", "The Eastern Velvet Ant (Cow-Killer)" }

    @property
    def prey(self):
        return self.__prey
    
    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Hawaiian Happy-Face Spider ate {prey} for a meal')
        else:
            print(f'The Hawaiian Happy-Face Spider rejects the {prey}')
    
    def __str__(self):
        return f'Hawaiian Happy-Face Spider {self.id}.'