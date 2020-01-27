from animals import RiverDolphin
from biomes.coastline import Coastline
from actions.biome_menu import biome_menu

def release_animal(arboretum):
    animal = None

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
        animal_to_release = RiverDolphin()
        pass
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