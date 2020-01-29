import os
from animals import river_dolphin
from animals import goldDustDayGecko
from animals import HappyFaceSpider
from animals import Kikakapu
from animals import neneGoose
from animals import opeapea
from animals import pueo
from animals import ulae
from interfaces.habitats.grasslandy import Grasslandy
from interfaces.animals.freshwater import IsFreshwater
# from interfaces.habitats.foresty import Forest
# from interfaces.habitats.stagnanty import Stagnant
# from interfaces.habitats.mountainy import Mountainy
from biomes.coastline import Coastline
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
    # Setting up an empty container for instances of each to go into when released.
    home_sweet_home = []
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
        animal = goldDustDayGecko()
        print('Gold Dust Day Gecko Was Added too ?')
    
    if choice == "2":
        animal = river_dolphin()
        print('Dolphin was added to ?')
    
    if choice == "3":
        animal = neneGoose()
        print('NeNe goose went somewhere ?')
    
    if choice == "4":
        animal = Kikakapu()
        print('Kikakapu go down the hole...')
    
    if choice == "5":
        animal = pueo()
        print('Pueo is a... animal. that goes places ?')
    
    if choice == "6":
        animal = ulae()
        print('Ulae where art thou? Ulae?')
    
    if choice == "7":
        animal = opeapea()
        print('Opeapea this guy a visit if you can find him...')
    
    if choice == "8":
        animal = HappyFaceSpider()
        print('Happy Face Spider goes.. let us be honest no one cares as long as it is not around. It is a spider.')
        
    else:
        input("Hey that is not an acceptabe answer.")
        return
        #trying to write a loop with isinstance: which is a built in function that can check if my object is a type or not. Using it to check for instance of each animal and initiate append. 
    if isinstance(animal, Grasslandy):
        for eachitem in arboretum.rivers:
            home_sweet_home.append(eachitem)
            
    if isinstance(animal, IsFreshwater):
        for eachitem in arboretum.rivers:
            home_sweet_home.append(eachitem)
            
    # for index, biome in enumerate(home_sweet_home):
    #     print(f'{index + 1}. {biome.name} ({len(biome.animals)})')

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