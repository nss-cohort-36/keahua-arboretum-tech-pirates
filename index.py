# Authors: Sam Pita, Christian Pippin, Jeremiah Bell, Charles Jackson, Caroline Brownlee

import os
from arboretum import Arboretum
from actions.annex import annex_habitat
from actions.release_animal import release_animal
from actions.report import build_facility_report
from actions.cultivate_plant_menu import cultivate_plant_menu

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Annex Habitat")
    print("2. Release Animal into Habitat")
    print("3. Feed Animal")
    print("4. Cultivate New Plant")
    print("5. Display Facility Report")
    print("6. Exit")


def main_menu():
    """Show Keahua Action Options

    Arguments: None
    """
    build_menu()
    choice = input(">> ")

    if choice == "1":
        annex_habitat(keahua)

    if choice == "2":
        release_animal(keahua)

    if choice == "3":
        pass
    # Need to add Logic for This option to do something other than nothing. Need to also build menu for htis to go to once it is used. 

    if choice == "4":
        cultivate_plant_menu(keahua)

    if choice == "5":
        build_facility_report(keahua)
        pass

    if choice != "6":
        main_menu()

main_menu()

# FIX Errors
# Error 1: Circular Import found at freshwater.py and fixed via path alteration. Reference site StackAbuse or Overflow
# 