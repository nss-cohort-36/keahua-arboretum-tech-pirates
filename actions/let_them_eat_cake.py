# Import Animals To Feed Cake (CritterVittles)
# import prey for animals to be fed cake
from animals.animal import Animal

# define a function to handle displaying the animals to feed once selected.

def animal_to_feed_cake(animal):
    return animal

# define a function to handle feeding Critters:
def critter_is_caked(animal):
    print(f'1. {animal.critter[0]}')
    print(f'2. {animal.critter[1]}')
    print(f'3. {animal.critter[2]}')
    print(f'4. {animal.critter[3]}')
    print(f'5. {animal.critter[4]}')
    print(f'6. {animal.critter[5]}')
    
    selection = input("Choose a healthy and humane snack for your critter pal! >>>")
    
    if selection == "1":
        print(f'{animal.animal} recieves {animal.critter[0]}')
    # write logic for more




