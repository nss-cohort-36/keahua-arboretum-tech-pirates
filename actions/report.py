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
            print(f'>>{animal.species}')
        for plant in river.plants:
            print(f'>>{plant.species}')
    
    # for mountain
    for mountain in arboretum.biomes["Mountains"]:
        print(f'Mountain [{mountain.id}]')
        for animal in mountain.animals:
            print(f'>>{animal.species}')
        for plant in mountain.plants:
            print(f'>>{plant.species}')
    
    # for grassland
    for grassland in arboretum.biomes["Grasslands"]:
        print(f'Grassland [{grassland.id}]')
        for animal in grassland.animals:
            print(f'>>{animal.species}')
        for plant in grassland.plants:
            print(f'>>{plant.species}')
    
    # for forest
    for forest in arboretum.biomes["Forests"]:
        print(f'Forest [{forest.id}]')
        for animal in forest.animals:
            print(f'>>{animal.species}')
        for plant in forest.plants:
            print(f'>>{plant.species}')
    
    # for swamp
    for swamp in arboretum.biomes["Swamps"]:
        print(f'Swamp [{swamp.id}]')
        for animal in swamp.animals:
            print(f'>>{animal.species}')
        for plant in swamp.plants:
            print(f'>>{plant.species}')
    
    # for coastline
    for coastline in arboretum.biomes["Coastlines"]:
        print(f'Coastline [{coastline.id}]')
        for animal in coastline.animals:
            print(f'>>{animal.species}')
        for plant in coastline.plants:
            print(f'>>{plant.species}')
    
    # -SP
    input("\n\nPress any key to continue...")