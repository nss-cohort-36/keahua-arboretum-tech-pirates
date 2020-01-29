import os
import sys
sys.path.append('../')
from arboretum import Arboretum

def biome_menu(arboretum):

    os.system('clear' if os.name == 'nt' else 'clear')
    # x = 1
    
    # biome_types = [Arboretum.rivers, Arboretum.grasslands, Arboretum.mountains, Arboretum.forests, Arboretum.swamps, Arboretum.coastlines
    # ]
    
    # iterate through the biomes dictionary in Arboretum()
    
    for index, biome in enumerate(arboretum.biomes):
        print({index + 1}, biome)
    
    choice = input("Choose a biome type for your plant > ")








    # capture user input
    # use index position
    # if choice == "1":
    #     River.add_plant(plant)
    
    # if choice == "2":
    #     Coastline.add_plant(plant)
    
    # if choice == "3":
    #     Mountain.add_plant(plant)
    
    # if choice == "4":
    #     Grassland.add_plant(plant)
        
    # if choice == "5":
    #     Swamp.add_plant(plant)
    
    # if choice == "6":
    #     Forest.add_plant(plant)
    

