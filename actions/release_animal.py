from animals import RiverDolphin
from biomes.coastline import Coastline

def release_animal(arboretum):
    animal = None

    print("1. River Dolphin")
    print("2. Dragonfly")

    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = RiverDolphin()

    if choice == "2":
        pass


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