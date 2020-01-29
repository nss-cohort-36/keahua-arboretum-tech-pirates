# ********************************************************************************************************************
# This file defines the Arboretum class which houses all of the biomes
# ********************************************************************************************************************

# Jb Personal Comments: Setting an initialized class. Blueprint for creation of objects. Lists set for individual Biomes. Is imported by Index.py
# Jb Question: Do we need to feed in the Lists and if not Why not?


class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.biomes = dict()
        # 6 Plants 6 Animals
        self.biomes["Rivers"] = []
        # 15 Plants 22 Animals
        self.biomes["Grasslands"] = []
        # Jb Personal Comments: Code so I can play and attempt to write some for my feeding project. NOT cowboying will Commment this out and will explain if asked. will delete off branch and move to different personal Branch if necessary.
        # 4 Plants 6 Animals
        self.biomes["Mountains"] = []

        self.biomes["Forests"] = []
        # 12 Plants 8 Animals
        self.biomes["Swamps"] = []
        # 3 Plants 15 Animals
        self.biomes["Coastlines"] = []

    # @property
    # def rivers(self):
    #     return self.__rivers

    # @property
    # def mountains(self):
    #     return self.__mountains

    # @property
    # def grasslands(self):
    #     return self.__grasslands

    # @property
    # def forests(self):
    #     return self.__forests

    # @property
    # def swamps(self):
    #     return self.__swamps

    # @property
    # def coastlines(self):
    #     return self.__coastlines