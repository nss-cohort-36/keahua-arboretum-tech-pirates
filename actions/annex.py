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
# from index import main_menu
#add imports for rest of biomes

# cp Need to add proper imports
def annex_biome(arboretum):
    os.system('clear' if os.name == 'nt' else 'clear')
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Mountain")
    print("6. Forest")
    # print("7. Main Menu")
    choice = input("Choose your biome to annex > ")
# cp Need to change strings to display appropriately based on the README
    if choice == "1":
        river = River()
        arboretum.biomes["Rivers"].append(river)
    if choice == "2":
        swamp = Swamp()
        arboretum.biomes["Swamps"].append(swamp)
    if choice == "3":
        coastline = Coastline()
        arboretum.biomes["Coastlines"].append(coastline)
    if choice == "4":
        grassland = Grassland()
        arboretum.biomes["Grasslands"].append(grassland)
    if choice == "5":
        mountain = Mountain()
        arboretum.biomes["Mountains"].append(mountain)
    if choice == "6":
        forest = Forest()
        arboretum.biomes["Forests"].append(forest)
    # if choice == "7":
    #     main_menu(keahua)
# cp Need to add functionality for append options
# cp Need to create files and classes for all missing biomes