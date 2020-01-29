import os
from biomes.river import River
from biomes.coastline import Coastline

def build_facility_report(arboretum):
    os.system('clear' if os.name == 'nt' else 'clear')
    print('Facility Report')
    
    # write logic for "if river is empty, then print(River: No river biomes currently in arboretum)"
    for river in arboretum.biomes["Rivers"]:
        print(f'River [{river.id}]')
        for animal in river.animals:
            print(f'{river.animal}')
    
    # for mountain
    for mountain in arboretum.biomes["Mountains"]:
        print(f'Mountain [{mountain.id}]')
    
    # for grassland
    for grassland in arboretum.biomes["Grasslands"]:
        print(f'Grassland [{grassland.id}]')
    
    # for forest
    for forest in arboretum.biomes["Forests"]:
        print(f'Forest [{forest.id}]')
    
    # for swamp
    for swamp in arboretum.biomes["Swamps"]:
        print(f'Swamp [{swamp.id}]')
    
    # for coastline
    for coastline in arboretum.biomes["Coastlines"]:
        print(f'Coastline [{coastline.id}]')
    
    # -SP
    input("\n\nPress any key to continue...")