# Jb-Comment: Imports Go up TOP!!!
import sys
sys.path.append('../')
from animals.preyCritters import preyLists
from animals.river_dolphin import RiverDolphin
import os
# Define Calls for Each animal

# Jb-Comment: Based on the instructions seems like I will need to make a menu for when someone selects feed animal to display a list of the animals and allow them to be fed.

def animal_to_feed_menu(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. KiKakapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")
    
    choice = input("Pick a Friendly Critter! They Need Noms! >>>")
    
    if choice == "1":
        prey_lists(arboretum)
    if choice == "2":
        pass
    if choice == "3":
        pass
    if choice == "4":
        pass
    if choice == "5":
        pass
    if choice == "6":
        pass
    if choice == "7":
        pass
    if choice == "8":
        pass
    count = 0
    animal_list = []
    
def prey_lists(arboretum):
    # os.system('cls' if os.name == 'nt' else 'clear')
    print(f'1. {preyLists.fish}')
    
    