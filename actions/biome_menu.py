import os
import sys
sys.path.append('../')
from arboretum import Arboretum
from biomes import River
from biomes import Swamp
from biomes import Coastline
from biomes import Grassland
from biomes import Forest
from biomes import Mountain

def biome_menu(arboretum, plant):
    print(plant)

    os.system('clear' if os.name == 'nt' else 'clear')
    # x = 1
    
    # biome_types = [Arboretum.rivers, Arboretum.grasslands, Arboretum.mountains, Arboretum.forests, Arboretum.swamps, Arboretum.coastlines
    # ]


    # Create empty list
    biomes_to_display = list()
    
    # Loops through biomes dictionary, then loops through dictionary items, grabs the value of every instance and adds that value to our empty list
    for key, value in arboretum.biomes.items():
        biomes_to_display += value

    # Loops through our list, prints out a string with the index position plus one, the instance name, and the instance id
    for index, biome in enumerate(biomes_to_display):
        # The index + 1 is creating a logical list for the user instead of starting at index position 0
        print(f"{index +1} {biome.name} {biome.id}")
    
    # Prompts the user to choose a biome from our printed list
    choice = input("Choose a biome type for your plant > ")
    
    # Takes the users input and cancels out the index + 1 in order to select the correct index position
    user_input = int(choice) - 1
    
    # Grabs the altered user input, accesses that index position in our biomes_to_display list, and adds the selected plant to that instance
    biomes_to_display[user_input].add_plant(plant)


def animal_biome_menu(arboretum, animal):
    print(animal)

    os.system('clear' if os.name == 'nt' else 'clear')
    # x = 1
    
    # biome_types = [Arboretum.rivers, Arboretum.grasslands, Arboretum.mountains, Arboretum.forests, Arboretum.swamps, Arboretum.coastlines
    # ]


    # Create empty list
    biomes_to_display = list()
    
    # Loops through biomes dictionary, then loops through dictionary items, grabs the value of every instance and adds that value to our empty list
    for key, value in arboretum.biomes.items():
        biomes_to_display += value

    # Loops through our list, prints out a string with the index position plus one, the instance name, and the instance id
    for index, biome in enumerate(biomes_to_display):
        # The index + 1 is creating a logical list for the user instead of starting at index position 0
        print(f"{index +1} {biome.name} {biome.id}")
    
    # Prompts the user to choose a biome from our printed list
    choice = input("Choose a biome type for your animal > ")
    
    # Takes the users input and cancels out the index + 1 in order to select the correct index position
    user_input = int(choice) - 1
    
    # Grabs the altered user input, accesses that index position in our biomes_to_display list, and adds the selected plant to that instance
    biomes_to_display[user_input].add_animal(animal)