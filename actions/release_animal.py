from animals.river_dolphin import RiverDolphin
from biomes.coastline import Coastline
from actions.biome_menu import biome_menu
import os

def release_animal(arboretum):
    animal = None
    os.system('clear' if os.name == 'nt' else 'clear')

    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kikakapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("Choose animal to release > ")

    if choice == "1":
        # animal_to_release = 
        pass

    if choice == "2":
        animal = RiverDolphin()
    if choice == "3":
        pass
    if choice == "4":
        pass
    if choice == "5":
        pass
    if choice == "6":
        pass
    if choice == "7":
        pass
    if choice == "8":
        pass

    biome_menu(arboretum)

    if choice == "1":
        River.add_animal(animal)
        print('Dolphin was added to River')
    


# *******************************
# Charles To-do Notes
# *******************************
# Dragonfly should not be included in the relaease animals section on line 7
# animals that need to be added to this module: 
# 1. Gold Dust Day Gecko 
# 3. Nene Goose
# 4. Kīkākapu
# 5. Pueo
# 6. 'Ulae
# 7. Ope'ape'a
# 8. Happy-Face Spider