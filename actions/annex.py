import os
import sys
sys.path.append('../')
from arboretum import Arboretum
from biomes import River
from arboretum import Arboretum
from biomes import Swamp
from biomes.coastline import Coastline
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
    choice = input("Choose your biome to annex > ")
# cp Need to change strings to display appropriately based on the README
    if choice == "1":
        river = River()
        Arboretum.rivers.append(river)
    elif choice == "2":
        swamp = Swamp("swamp")
        Arboretum.swamps.append(swamp)
    elif choice == "3":
        coastline = Coastline()
        arboretum.coastline.append(coastline)
# cp Need to add functionality for append options
# cp Need to create files and classes for all missing biomes