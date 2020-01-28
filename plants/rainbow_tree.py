from plants import Plant
from interfaces.animals import IsFreshwater
from interfaces import Identifiable

class RainbowTree(Plant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree")
        Identifiable.__init__(self)
        self.__prey = { "Trout", "Mackarel", "Salmon", "Sardine" }

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