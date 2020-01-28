# ********************************************************************************************************************
# This file defines the Arboretum class which houses all of the biomes
# ********************************************************************************************************************

# Jb Personal Comments: Setting an initialized class. Blueprint for creation of objects. Lists set for individual Biomes. Is imported by Index.py
# Jb Question: Do we need to feed in the Lists and if not Why not?


class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        # 6 Plants 6 Animals
        self.__rivers = []
        # 15 Plants 22 Animals
        self.grasslands = []
        # Jb Personal Comments: Code so I can play and attempt to write some for my feeding project. NOT cowboying will Commment this out and will explain if asked. will delete off branch and move to different personal Branch if necessary.
        # 4 Plants 6 Animals
        self.__mountains = []

        self.forests = []
        # 12 Plants 8 Animals
        self.swamps = []
        # 3 Plants 15 Animals
        self.coastlines = []

    @property
    def rivers(self):
        return self.__rivers

    @property
    def mountains(self):
        return self.__mountains


# cp Need to create attributes for all missing biomes
