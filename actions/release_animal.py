import os
from animals import RiverDolphin
from interfaces.animals.grasslandy import Grasslandy

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

    elif choice == "2":
        animal = RiverDolphin()

    elif choice == "3":
        animal = NeneGoose()

    elif choice == "4":
        animal = Kikakapu()

    elif choice == "5":
        animal = Pueo()

    elif choice == "6":
        animal = Ulae()

    elif choice == "7":
        animal = Opeapea()

    elif choice == "8":
        animal = HappySpider()
        
    else:
        input(" That sucked try again! ")
        return
    
    if isinstance(animal, Grasslandy):
        for eachitem in arboretum.grasslands:
            arboretum.grasslands.append(eachitem)


    # for index, river in enumerate(arboretum.rivers):
    #     print(f'{index + 1}. River {river.id}')

    print("Release the animal into which biome?")
    choice = input("> ")

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