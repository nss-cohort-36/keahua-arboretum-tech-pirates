from animals import Animal
from interfaces.animals import IsFreshwater
from interfaces.animals.grasslandy import Grasslandy
from interfaces import Identifiable

class RiverDolphin(Animal, IsFreshwater, Identifiable):

    def __init__(self):
        Animal.__init__(self, "River dolphin")
        IsFreshwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Yellow Fin Tuna", "Mahi-Mahi", "Marlin", "Wahoo", "Ono", "Hapu'upu'u", "Kajiki", "Opakapaku", "Monchong" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The dolphin ate {prey} for a meal')
        else:
            print(f'The dolphin rejects the {prey}')


    def __str__(self):
        return f'Dolphin {self.id}. Eeee EeeEEeeeeEE!'
