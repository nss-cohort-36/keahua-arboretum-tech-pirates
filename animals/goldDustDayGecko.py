from interfaces.animals import IsTerrestrial
from animals import Animal
from interfaces import Identifiable

class Gold_Dust_Day_Gecko(Animal, IsTerrestrial, Identifiable):
    def __init__(self):
        Animal.__init__(self, "Gold Dust Day Gecko")
        IsTerrestrial.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Centipedes", "Cockroaches", "Assassin Bug", "Golden Tortoise Beetle", "Dobsonflies", "The Eastern Velvet Ant (Cow-Killer)" }

    @property
    def prey(self):
        return self.__prey
    
    def feed(self, prey):
        if prey in self.__prey:
            print(f'The gold dust day gecko ate {prey} for a meal')
        else:
            print(f'The gold dust day gecko rejects the {prey}')
    
    def __str__(self):
        return f'Gold Dust Day Geckos {self.id}.'