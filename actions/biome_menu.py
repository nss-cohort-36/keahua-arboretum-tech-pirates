import os

def biome_menu(arboretum):

    os.system('clear' if os.name == 'nt' else 'clear')

    for index, river in enumerate(arboretum.biome_list):
        print(f'{index + 1}. River {river.id}')

    for index, coastline in enumerate(arboretum.coastlines):        print(f'{index + 1}. Coastline {coastline.id}')

    for index, mountain in enumerate(arboretum.mountains):
        print(f'{index + 1}. Mountain {mountain.id}')

    for index, grassland in enumerate(arboretum.grasslands):
        print(f'{index + 1}. Grassland {grassland.id}')

    for index, swamp in enumerate(arboretum.swamps):
        print(f'{index + 1}. Swamp {swamp.id}')

    for index, forest in enumerate(arboretum.forests):
        print(f'{index + 1}. Forest {forest.id}')

    choice = input("Release the animal into which biome? >")

    arboretum.rivers[int(choice) - 1].animals.append(animal)