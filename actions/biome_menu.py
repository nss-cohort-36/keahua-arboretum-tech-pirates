import os
from biomes.river import River

def biome_menu(arboretum):

    os.system('clear' if os.name == 'nt' else 'clear')
    
    for index, river in enumerate(arboretum.rivers):
        print(f'{index + 1}. River {river.id}')

    for index, coastline in enumerate(arboretum.coastlines):
        print(f'{index + 2}. Coastline {coastline.id}')

    for index, mountain in enumerate(arboretum.mountains):
        print(f'{index + 3}. Mountain {mountain.id}')

    for index, grassland in enumerate(arboretum.grasslands):
        print(f'{index + 4}. Grassland {grassland.id}')

    for index, swamp in enumerate(arboretum.swamps):
        print(f'{index + 5}. Swamp {swamp.id}')

    for index, forest in enumerate(arboretum.forests):
        print(f'{index + 6}. Forest {forest.id}')

    