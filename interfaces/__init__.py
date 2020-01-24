from .animals.terrestrial import IsTerrestrial
from .animals.freshwater import IsFreshwater
from interfaces.animals.aquatic import IsAquatic
from .animals.actions.flying import IsFlying
from .animals.actions.walking import IsWalking
from .animals.actions.swimming import IsSwimming
from .identifiable import Identifiable
from .habitats.contains_animals import IContainsAnimals
from .habitats.contains_plants import IContainsPlants

# CJ Note: Based on my findings in the multiple inheritance chapter, the IContainsAnimals, IContainsPlants on lines 8 and 9 in this module may need to be put in an __init__.py file within the habitats folder. Reference the following link:https://github.com/nashville-software-school/bangazon-llc/blob/master/book-1-orientation/chapters/MULTIPLE_INHERITANCE.md#update-the-movements-package