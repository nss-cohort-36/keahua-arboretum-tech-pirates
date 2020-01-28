from interfaces.animals import IsFreshwater
from animals import Animal
from interfaces import Identifiable

class Kīkākapu(Animal, IsFreshwater, Identifiable):
    def __init__(self):
        Animal.__init__(self, "Nene Goose")
        IsFreshwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Yellow Fin Tuna", "Mahi-Mahi", "Marlin", "Wahoo", "Ono", "Hapu'upu'u", "Kajiki", "Opakapaku", "Monchong" }

    @property
    def prey(self):
        return self.__prey
    
    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Kīkākapu ate {prey} for a meal')
        else:
            print(f'The Kīkākapu rejects the {prey}')
    
    def __str__(self):
        return f'Kīkākapu {self.id}.'
    
