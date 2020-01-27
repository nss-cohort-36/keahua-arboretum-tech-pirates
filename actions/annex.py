import os
import sys
sys.path.append('../')
from arboretum import Arboretum
from biomes.river import River
from biomes.swamp import Swamp
from biomes.coastline import Coastline
from biomes.grassland import Grassland
from biomes.forest import Forest
from biomes.mountain import Mountain
# from index import main_menu
#add imports for rest of biomes

# cp Need to add proper imports
def annex_biome(Arboretum):
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
        Arboretum.rivers.append(river)
    elif choice == "2":
        swamp = Swamp("swamp", 12, 8)
        Arboretum.swamps.append(swamp)
    elif choice == "3":
        coastline = Coastline()
        Arboretum.coastlines.append(coastline)
    if choice == "4":
        grassland = Grassland()
        Arboretum.grasslands.append(grassland)
    if choice == "5":
        mountain = Mountain()
        Arboretum.mountains.append(mountain)
    if choice == "6":
        forest = Forest()
        Arboretum.forests.append(forest)
    # if choice == "7":
    #     main_menu(keahua)
# cp Need to add functionality for append options
# cp Need to create files and classes for all missing biomes