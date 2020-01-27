from interfaces.animals import IsTerrestrial
from animals import Animal
from interfaces import Identifiable

class Pueo(Animal, IsTerrestrial, Identifiable):
    def __init__(self):
        