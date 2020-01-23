import os
from arboretum import Arboretum
from actions.annex import annex_habitat
from actions.release_animal import release_animal
from actions.report import build_facility_report
# ADDED THIS IMPORT TO PRODUCE MENU WHEN NUMBER 4 IS CHOSEN. NEEDS TO BE UNCOMMENTED FOR CODE ON CHOICE 4 TO WORK:
# from actions.cultivate_plant import cultivate_plant

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

# NEED FUNCTIONALITY THAT WILL DISPLAY THE FOLLOWING MENU WHEN 4 IS PRESSED:
# Added cultivate_plant.py in actions folder to hold the code to display this menu. WORKS!
    if choice == "4":
        pass
        # the following method needs to be uncommented and "pass" removed:

        # cultivate_plant(keahua)

    if choice == "5":
        build_facility_report(keahua)
        pass

    if choice != "6":
        main_menu()

main_menu()

# FIX Errors
# Error 1: Circular Import found at freshwater.py and fixed via path alteration. Reference site StackAbuse or Overflow