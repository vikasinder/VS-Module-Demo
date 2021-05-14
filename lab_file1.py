# Labfilemodule2 is imported ( all the files are imported )
from labfile2module import *
# Python package of colorama module is imported to add text styles
from colorama import Fore, Back, Style

# Instance of class is created
member1 = area_parameters_volume()

print(Fore.LIGHTMAGENTA_EX)
print(Back.RESET)
print("\n********* Python Module and Packages Assignment **********\n")

# This Loop is going to run unless user wants to exit the program

while input(" Do You Want To Continue? [y/n] : ") == "y":
    try:
        print(Fore.YELLOW)
        print(Back.RESET)
        print("\n***** MENU *****\n")

        # Input To get user choice:

        value = int(input(
            "Choose what you want to calculate :\n\n Enter 1. To Calculate Area  \n Enter 2. To Calculate Perimeter  \n Enter 3. To Calculate Volume  \n Enter 0. For Exit : "))
        # if - else condition
        if value == 1 or value == 2 or value == 3:

            # Option function within class 'area_parameters_volume' is called
            # value as an argument is passed to the function
            # And returned  calculated value is assigned to answer Variable

            answer = member1.option(value)
            print(Fore.LIGHTCYAN_EX)
            print(Style.DIM)

            # The result is then printed on to the screen

            print(f"Your Calculated Value is : {answer}\n")
        elif value == 0:
            print(Fore.RED)
            break
        else:
            print(Fore.RED)
            print(Back.WHITE)
            raise TypeError
    except TypeError:
        # If the value entered is not the accepted values it will raise this error
        print("\n You entered wrong Input. Please Try again.\n")
    except ValueError:
        print(Fore.RED)
        # If the value entered is not the accepted values it will raise this error
        print(
            f"\nInvalid data:  Please enter either 1 - 2 - 3 Or 0 to Exit.\n")
