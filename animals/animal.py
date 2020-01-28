class Animal:

    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = 0
       

    def move(self, propulsion, speed):
        return f"{self. species} moves at {speed} meters/sec by {propulsion}"


@property
def prey(self):
    return self.__food