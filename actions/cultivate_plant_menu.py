# Author: caroline brownlee

import os
import sys
sys.path.append('../')
# from arboretum import Arboretum
from biomes import River
from biomes import Swamp
from biomes import Coastline
from biomes import Grassland
from biomes import Forest
from biomes import Mountain
from plants import Blue_Jade_Vine
from plants import Mountain_Apple_Tree
from plants import RainbowTree
from plants import Silversword
from .biome_menu import biome_menu
# from index import main_menu

def cultivate_plant_menu(arboretum):
    plant = None
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")
    print("5. Main Menu")

    choice = input("Choose plant to culitivate > ")

    if choice == "1":
        plant = RainbowTree()
    
    if choice == "2":
        plant = Silversword()

    if choice == "3":
        plant = Blue_Jade_Vine()

    if choice == "4":
        plant = Mountain_Apple_Tree()

    # if choice == "5":
        
    biome_menu(arboretum, plant)

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
# ((((ISSUE: Per README, NEED FUNCTIONALITY THAT WILL PRODUCE THE FOLLOWING WHEN ONE OF THOSE CHOICES ARE MADE))))

# 1. Grassland (5 plants)
# 2. Swamp (2 plants)
# 3. Swamp (9 plants)
# 4. Swamp (0 plants)

# Where would you like to plant the Sun Jade Vine?
# > _ 