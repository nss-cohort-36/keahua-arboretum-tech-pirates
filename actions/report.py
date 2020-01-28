import os
from biomes.river import River
def build_facility_report(arboretum):
    os.system('clear' if os.name == 'nt' else 'clear')
    print('Facility Report')
    
    # write logic for "if river is empty, then print(River: No river biomes currently in arboretum)"
    for river in arboretum.rivers:
        print(f'River [{river.id}]')
        print(f'{River.animals[0]}')
    
    # for mountain
    for mountain in arboretum.mountains:
        print(f'Mountain [{mountain.id}]')
    
    # for grassland
    for grassland in arboretum.grasslands:
        print(f'Grassland [{grassland.id}]')
    
    # for forest
    for forest in arboretum.forests:
        print(f'Forest [{forest.id}]')
    
    # for swamp
    for swamp in arboretum.swamps:
        print(f'Swamp [{swamp.id}]')
    
    # for coastline
    for coastline in arboretum.coastlines:
        print(f'Coastline [{coastline.id}]')
    
    # -SP
    input("\n\nPress any key to continue...")