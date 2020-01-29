import os
from animals import river_dolphin
from animals import goldDustDayGecko
from animals import HappyFaceSpider
from animals import Kikakapu
from animals import neneGoose
from animals import opeapea
from animals import pueo
from animals import ulae
from interfaces.animals.grasslandy import Grasslandy
from biomes.coastline import Coastline
from actions.biome_menu import biome_menu

def release_animal(arboretum):
    animal = None
    os.system('cls' if os.name == 'nt' else 'clear')
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
        animal = goldDustDayGecko()

    if choice == "2":
        animal = river_dolphin()
    
    if choice == "3":
        animal = neneGoose()

    if choice == "4":
        animal = Kikakapu()

    if choice == "5":
        animal = pueo()

    if choice == "6":
        animal = ulae()

    if choice == "7":
        animal = opeapea()

    if choice == "8":
        animal = HappyFaceSpider()
        
    else:
        input(" That sucked try again! ")
        return

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