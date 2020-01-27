import os
from animals import RiverDolphin
from interfaces.animals.grasslandy import Grasslandy
from biomes.coastline import Coastline

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
        animal = GoldGecko()

    if choice == "2":
        animal = RiverDolphin()

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

    if choice == "8":
        animal = HappySpider()
        
    else:
        input(" That sucked try again! ")
        return

    for index, river in enumerate(arboretum.rivers):
        print(f'Rivers:')
        print(f'{index + 1}. River {river.id}')

    for index, coastline in enumerate(arboretum.coastlines):
        print(f'Coastlines:')
        print(f'{index + 1}. Coastline {coastline.id}')
    
    for index, mountain in enumerate(arboretum.mountains):
        print(f'Mountains:')
        print(f'{index + 1}. Mountain {mountain.id}')

    for index, grassland in enumerate(arboretum.grasslands):
        print(f'Grasslands:')
        print(f'{index + 1}. Grassland {grassland.id}')

    for index, swamp in enumerate(arboretum.swamps):
        print(f'Swamps:')
        print(f'{index + 1}. Swamp {swamp.id}')

    for index, forest in enumerate(arboretum.forests):
        print(f'Forests:')
        print(f'{index + 1}. Forest {forest.id}')

    
    choice = input("Release the animal into which biome? >")

    if choice == "3":
        Coastline.add_animal(animal)

    arboretum.rivers[int(choice) - 1].animals.append(animal)


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