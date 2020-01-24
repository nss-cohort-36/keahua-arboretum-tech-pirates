# Jb Personal Comments: Setting an initialized class. Blueprint for creation of objects. Lists set for individual Biomes. Is imported by Index.py
# Jb Question: Do we need to feed in the Lists and if not Why not?
class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        # 6 Plants 6 Animals
        self.rivers = []
        # 15 Plants 22 Animals
        self.grasslands = []
        # Jb Personal Comments: Code so I can play and attempt to write some for my feeding project. NOT cowboying will Commment this out and will explain if asked. will delete off branch and move to different personal Branch if necessary.
        # 4 Plants 6 Animals
        self.mountains = []
        # 32 plants 20 Animals
        self.forests = []
        # 12 Plants 8 Animals
        self.swamps = []
        # 3 Plants 15 Animals
        self.coastlines = []


# FROM README
# class Arboretum:

#     def __init__(self):
#         self.__rivers = []

#     @property
#     def rivers(self):
#         return self.__rivers

#     def annex_river(self, river):
#         self.__rivers.append(river)
# cp Need to create attributes for all missing biomes
