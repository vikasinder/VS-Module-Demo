# Class is declared That contains all the functions and variable
class Area_parameters_volume:
    # Global single variable is declared that gets the calculated result
    calculate = 0
# Option function is declared that is called on lab_file1 page

    def option(self, value):
        # Condition to check value to be calculated bt the user:
        if(value == 1):
            return (self.area())
        elif(value == 2):
            return (self.perimeter())
        else:
            return (self.volume())

# Area function is declared to calculate area and pass the calculated result on the screen
    def area(self):
        print("\n ****Calculate Area **** \n")

        while True:
            try:
                # Global keyword is used , so as to declare that calculate is a global variable
                global calculate
                area = int(input(
                    "Choose what you want to calculate :\n\n Enter 1. Area of Square \n Enter 2. Area Of rectangle  \n Enter 3. Area of circle \n Enter 0. To Exit : "))
                if(area == 1):
                    # Loop will run unless the conditions are not met ( To keep check on redundancy)
                    while True:
                        try:
                            side = float(input("\nEnter Side Of square : "))
                            if side < 0:
                                raise TypeError
                            else:
                                calculate = side ** 2
                                return calculate
                        except TypeError as error:
                            print(
                                f"\nInvalid Entry: {error}. Please provide a positive number.\n")
                        except ValueError as error:
                            print(
                                f"\nInvalid Entry: {error}. Please enter an integer or float value.\n")

                elif(area == 2):
                    # Loop will run unless the conditions are not met ( To keep check on redundancy)
                    while True:
                        try:
                            length = float(
                                input("\nEnter Length Of Rectangle : "))
                            width = float(
                                input("\nEnter width Of Rectangle : "))
                            if length < 0:
                                raise TypeError
                            if width < 0:
                                raise TypeError
                            else:
                                calculate = length*width
                                return calculate
                        except TypeError as error:
                            print(
                                f"\nInvalid Entry: {error}. Please provide a positive number.\n")
                        except ValueError as error:
                            print(
                                f"\nInvalid Entry:{error}  Please enter an integer or float value.\n")

                elif(area == 3):
                   # Loop will run unless the conditions are not met ( To keep check on redundancy)
                    while True:
                        try:
                            radius = float(
                                input("\nEnter Radius Of circle : "))
                            if radius < 0:
                                raise TypeError
                            else:
                                calculate = radius ** 2 * 3.14
                                return calculate
                        except TypeError as error:
                            print(
                                f"\nInvalid Entry: {error}. Please provide a positive number.\n")
                        except ValueError as error:
                            print(
                                f"\nInvalid Entry:{error}  Please enter an integer or float value.\n")

                elif(area == 0):
                    return "Thanks For Using This Program"
                else:
                    raise TypeError
            except TypeError:
                print("\nYou entered wrong Input. Please Try again.\n")
            except ValueError:
                print(
                    f"\nInvalid choice: {area}  Please enter either 1 - 2 - 3 \n")

# Perimeter function is declared to calculate perimeter and pass the calculated result on the screen

    def perimeter(self):
        print("\n **** Calculate Perimeter **** \n")

      # Loop will run unless the conditions are not met ( To keep check on redundancy)

        while True:
            try:
              # Global keyword is used , so as to declare that calculate is a global variable
                global calculate
                Perimeter = int(input(
                    "Choose what you want to calculate :\n\n Enter 1. Perimeter of Square \n Enter 2. Perimeter Of rectangle  \n Enter 3. Perimeter of circle \n Enter 0. To Exit : "))
                if(Perimeter == 1):
                    # Loop will run unless the conditions are not met ( To keep check on redundancy)

                    while True:
                        try:
                            side = float(input("\nEnter Side Of square : "))
                            if side < 0:
                                raise TypeError
                            else:
                                calculate = side * 4
                                return calculate
                        except TypeError as error:
                            print(
                                f"\nInvalid Entry: {error}. Please provide a positive number.\n")
                        except ValueError as error:
                            print(
                                f"\nInvalid Entry: {error}. Please enter an integer or float value.\n")

                elif(Perimeter == 2):
                  # Loop will run unless the conditions are not met ( To keep check on redundancy)

                    while True:
                        try:
                            length = float(
                                input("\nEnter Length Of Rectangle : "))
                            width = float(
                                input("\nEnter width Of Rectangle : "))
                            if length < 0:
                                raise TypeError
                            if width < 0:
                                raise TypeError
                            else:
                                calculate = 2*(length+width)
                                return calculate
                        except TypeError as error:
                            print(
                                f"\nInvalid Entry: {error}. Please provide a positive number.\n")
                        except ValueError as error:
                            print(
                                f"\nInvalid Entry:{error}  Please enter an integer or float value.\n")

                elif(Perimeter == 3):
                  # Loop will run unless the conditions are not met ( To keep check on redundancy)

                    while True:
                        try:
                            radius = float(
                                input("\nEnter Radius Of circle : "))
                            if radius < 0:
                                raise TypeError
                            else:
                                calculate = radius * 2 * 3.14
                                return calculate
                        except TypeError as error:
                            print(
                                f"\nInvalid Entry: {error}. Please provide a positive number.\n")
                        except ValueError as error:
                            print(
                                f"\nInvalid Entry: {error}. Please enter an integer or float value.\n")

                elif(Perimeter == 0):
                    return "Thanks For Using This Program"
                else:
                    raise TypeError
            except TypeError:
                print("\nYou entered wrong Input. Please Try again.\n")
            except ValueError:
                print(
                    f"\nInvalid choice: {Perimeter}  Please enter either 1 - 2 - 3 \n")
# Volume function is declared to calculate volume and pass the calculated result on the screen

    def volume(self):
        print("\n **** Calculater Volume **** \n")
        # Loop will run unless the conditions are not met ( To keep check on redundancy)

        while True:
            try:
              # Global keyword is used , so as to declare that calculate is a global variable
                global calculate
                volume = int(input(
                    "Choose what you want to calculate :\n\n Enter 1. Volume of Cube \n Enter 2. Volume Of Cylinder  \n Enter 3. Volume of Sphere \n Enter 0. To Exit : "))
                if(volume == 1):

                    # Loop will run unless the conditions are not met ( To keep check on redundancy)

                    while True:
                        try:
                            side = float(input("\nEnter Side Of cube : "))
                            if side < 0:
                                raise TypeError
                            else:
                                calculate = side ** 3
                                return calculate
                        except TypeError as error:
                            print(
                                f"\nInvalid Entry: {error}. Please provide a positive number.\n")
                        except ValueError as error:
                            print(
                                f"\nInvalid Entry: {error}. Please enter an integer or float value.\n")

                elif(volume == 2):

                    # Loop will run unless the conditions are not met ( To keep check on redundancy)

                    while True:
                        try:
                            radius = float(
                                input("\nEnter Radius Of Cylinder : "))
                            height = float(
                                input("\nEnter height Of Cylinder : "))
                            if radius < 0:
                                raise TypeError
                            if height < 0:
                                raise TypeError
                            else:
                                calculate = 3.14 * radius ** 2 * height
                                return calculate
                        except TypeError as error:
                            print(
                                f"\nInvalid Entry: {error}. Please provide a positive number.\n")
                        except ValueError as error:
                            print(
                                f"\nInvalid Entry: {error}. Please enter an integer or float value.\n")

                elif(volume == 3):

                    # Loop will run unless the conditions are not met ( To keep check on redundancy)

                    while True:
                        try:
                            radius = float(
                                input("\nEnter Radius Of Sphere : "))
                            if radius < 0:
                                raise TypeError
                            else:
                                calculate = (4/3) * 3.14 * radius**3
                                return calculate
                        except TypeError as error:
                            print(
                                f"\nInvalid Entry: {error}. Please provide a positive number.\n")
                        except ValueError as error:
                            print(
                                f"\nInvalid Entry: {error}. Please enter an integer or float value.\n")

                elif(volume == 0):
                    # Returns "Thanks For Using This Program" if user wants to leave ther program
                    return "Thanks For Using This Program"

                else:
                    # If the value entered is not the accepted values it will raise this error
                    raise TypeError
            except TypeError:
                print("\nYou entered wrong Input. Please Try again.\n")
            except ValueError:
                # If the value entered is not the accepted values it will raise this error
                print(
                    f"\nInvalid choice: {volume}  Please enter either 1 - 2 - 3 \n")
