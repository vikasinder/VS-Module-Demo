from labfile2module import *


member1 = area_parameters_volume()

while input("Do You Want To Continue? [y/n] : ") == "y":
    try:
        print("\n***** MENU *****\n")
        value = int(input(
            "Choose what you want to calculate :\n Enter 1. To Calculate Area  \n Enter 2. To Calculate Perimeter  \n Enter 3. To Calculate Volume  \n Enter 0. For Exit : "))
        if value == 1 or value == 2 or value == 3:
            answer = member1.option(value)
            print(f"Your Calculated Value is : {answer}")
        elif value == 0:
            break
        else:
            raise TypeError
    except TypeError:
        print("You entered wrong Input. Please Try again.\n")
    except ValueError:
        print(
            f"Invalid data:  Please enter either 1 - 2 - 3 Or 0 to Exit.\n")
