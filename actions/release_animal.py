import os
from animals.river_dolphin import RiverDolphin
from animals.neneGoose import Nene_Goose
from animals.goldDustDayGecko import Gold_Dust_Day_Gecko
from animals.kikakapu import Kikakapu
from animals.pueo import Pueo
from animals.ulae import Ulae
from animals.opeapea import Opeapea
from animals.HappyFaceSpider import Hawaiian_Happy_Face_Spider
from actions.biome_menu import biome_menu

def release_animal(arboretum):
    animal = None
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kikakapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")

    choice = input("Choose animal to release into the chosen habitat > ")

    if choice == "1":
        animal = Gold_Dust_Day_Gecko()
    if choice == "2":
        animal = RiverDolphin()
    if choice == "3":
        animal = Nene_Goose()
    if choice == "4":
        animal = Kikakapu()
    if choice == "5":
        animal = Pueo()
    if choice == "6":
        animal = Ulae()
    if choice == "7":
        animal = Opeapea()
    if choice == "8":
        animal = Hawaiian_Happy_Face_Spider()    
    else:
        input(" That sucked try again! ")
        return

    choice = input("Release the animal into which biome? >")

    if choice == "1":
        River.add_animal()
    


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