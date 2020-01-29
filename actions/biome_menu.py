import os
import sys
sys.path.append('../')
from arboretum import Arboretum

def biome_menu(arboretum):

    os.system('clear' if os.name == 'nt' else 'clear')
    # x = 1
    
    # biome_types = [Arboretum.rivers, Arboretum.grasslands, Arboretum.mountains, Arboretum.forests, Arboretum.swamps, Arboretum.coastlines
    # ]
    
    
    
    for index, biome in enumerate(arboretum.biomes):
        print({index + 1}, biome)
    
    choice = input("Choose a biome type for your plant > ")

    if choice == "1":
        print()
    
    # capture user input
    # use index position
    if choice == "1":
        River.add_plant(plant)
    
    if choice == "2":
        Coastline.add_plant(plant)
    
    if choice == "3":
        Mountain.add_plant(plant)
    
    if choice == "4":
        Grassland.add_plant(plant)
        
    if choice == "5":
        Swamp.add_plant(plant)
    
    if choice == "6":
        Forest.add_plant(plant)
    # for index, river in enumerate(arboretum.rivers):
    #     print(f'{index + 1}. River {river.id}')

    # for index, coastline in enumerate(arboretum.coastlines):
    #     print(f'{index + 2}. Coastline {coastline.id}')

    # for index, mountain in enumerate(arboretum.mountains):
    #     print(f'{index + 3}. Mountain {mountain.id}')

    # for index, grassland in enumerate(arboretum.grasslands):
    #     print(f'{index + 4}. Grassland {grassland.id}')

    # for index, swamp in enumerate(arboretum.swamps):
    #     print(f'{index + 5}. Swamp {swamp.id}')

    # for index, forest in enumerate(arboretum.forests):
    #     print(f'{index + 6}. Forest {forest.id}')

# biome_types = [Arboretum.rivers, Arboretum.grasslands, Arboretum.mountains, Arboretum.forests, Arboretum.swamps, Arboretum.coastlines
# ]

# for index, biome_type in enumerate(biome_types):
#     print({index}, type)
