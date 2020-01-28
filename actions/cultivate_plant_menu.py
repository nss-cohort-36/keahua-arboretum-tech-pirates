# Author: caroline brownlee

import os
import sys
sys.path.append('../')
from arboretum import Arboretum
from plants import Blue_Jade_Vine
from plants import Mountain_Apple_Tree
from plants import RainbowTree
from plants import Silversword
# from index import main_menu

def cultivate_plant_menu(Arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")
    print("5. Main Menu")

    choice = input("Choose plant to culitivate > ")

    if choice == "1":
        plant_to_cultivate = RainbowTree()
     
    if choice == "2":
        plant_to_cultivate = Silversword()

    if choice == "3":
        plant_to_cultivate = Blue_Jade_Vine()

    if choice == "4":
        plant_to_cultivate = Mountain_Apple_Tree()

    # if choice == "5":
    #     main_menu()
    
# ((((ISSUE: Per README, NEED FUNCTIONALITY THAT WILL PRODUCE THE FOLLOWING WHEN ONE OF THOSE CHOICES ARE MADE))))

# 1. Grassland (5 plants)
# 2. Swamp (2 plants)
# 3. Swamp (9 plants)
# 4. Swamp (0 plants)

# Where would you like to plant the Sun Jade Vine?
# > _ 