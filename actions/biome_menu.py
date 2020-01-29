import os
import sys
sys.path.append('../')
from arboretum import Arboretum
from biomes import River
from biomes import Swamp
from biomes import Coastline
from biomes import Grassland
from biomes import Forest
from biomes import Mountain

def biome_menu(arboretum, plant):
    print(plant)

    os.system('clear' if os.name == 'nt' else 'clear')
    # x = 1
    
    # biome_types = [Arboretum.rivers, Arboretum.grasslands, Arboretum.mountains, Arboretum.forests, Arboretum.swamps, Arboretum.coastlines
    # ]


    
    biomes_to_display = list()
    
    #retrieve all keys/values in list
    for key, value in arboretum.biomes.items():
        biomes_to_display += value
        
    for index, biome in enumerate(biomes_to_display):
        print(f"{index +1} {biome.name} {biome.id}")
    
    choice = input("Choose a biome type for your plant > ")
    
    user_input = int(choice) - 1
    
    biomes_to_display[user_input].add_plant(plant)
    

    
    
    







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
    