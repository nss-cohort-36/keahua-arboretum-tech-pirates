<<<<<<< HEAD
import os
from animals import RiverDolphin
from interfaces.animals.grasslandy import Grasslandy
=======
from animals.river_dolphin import RiverDolphin
>>>>>>> master
from biomes.coastline import Coastline
from actions.biome_menu import biome_menu
import os

def release_animal(arboretum):
    animal = None
<<<<<<< HEAD
    os.system('cls' if os.name == 'nt' else 'clear')
=======
    os.system('clear' if os.name == 'nt' else 'clear')

>>>>>>> master
    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. KiKakapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("Choose animal to release into the chosen habitat > ")

    if choice == "1":
        animal = GoldGecko()

    if choice == "2":
        animal = RiverDolphin()
<<<<<<< HEAD

=======
>>>>>>> master
    if choice == "3":
        animal = NeneGoose()

    if choice == "4":
        animal = Kikakapu()

    if choice == "5":
        animal = Pueo()

    if choice == "6":
        animal = Ulae()

    if choice == "7":
        animal = Opeapea()

<<<<<<< HEAD
    if choice == "8":
        animal = HappySpider()
        
    else:
        input(" That sucked try again! ")
        return
=======
    biome_menu(arboretum)
>>>>>>> master

    if choice == "1":
        River.add_animal()
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