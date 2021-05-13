class area_parameters_volume:

    calculate = 0

    def option(self, value):

        if(value == 1):
            return (self.area())
        elif(value == 2):
            return (self.perimeter())
        else:
            return (self.volume())

    def area(self):
        print("\n **** Area **** \n")

        while True:
            try:
                global calculate
                area = int(input(
                    "Choose what you want to calculate :\n Enter 1. Area of Square \n Enter 2. Area Of rectangle  \n Enter 3. Area of circle \n Enter 0. To Exit : "))
                if(area == 1):
                    side = float(input("Enter Side Of square :"))
                    calculate = side ** 2
                    return calculate
                elif(area == 2):
                    length = float(input("Enter Length Of Rectangle : "))
                    width = float(input("Enter width Of Rectangle : "))
                    calculate = length*width
                    return calculate
                elif(area == 3):
                    radius = float(input("Enter Radius Of circle : "))
                    calculate = radius ** 2 * 3.14
                    return calculate
                elif(area == 0):
                    return "Thanks For Using This Program"
                else:
                    raise TypeError
            except TypeError:
                print("You entered wrong Input. Please Try again.\n")
            except ValueError:
                print(
                    f"Invalid choice: {area}  Please enter either 1 - 2 - 3 \n")

    def perimeter(self):
        print("\n **** Perimeter **** \n")

        while True:
            try:
                global calculate
                Perimeter = int(input(
                    "Choose what you want to calculate :\n Enter 1. Perimeter of Square \n Enter 2. Perimeter Of rectangle  \n Enter 3. Perimeter of circle \n Enter 0. To Exit : "))
                if(Perimeter == 1):
                    side = float(input("Enter Side Of square :"))
                    calculate = side * 4
                    return calculate
                elif(Perimeter == 2):
                    length = float(input("Enter Length Of Rectangle : "))
                    width = float(input("Enter width Of Rectangle : "))
                    calculate = 2*(length+width)
                    return calculate
                elif(Perimeter == 3):
                    radius = float(input("Enter Radius Of circle : "))
                    calculate = radius * 2 * 3.14
                    return calculate
                elif(Perimeter == 0):
                    return "Thanks For Using This Program"
                else:
                    raise TypeError
            except TypeError:
                print("You entered wrong Input. Please Try again.\n")
            except ValueError:
                print(
                    f"Invalid choice: {Perimeter}  Please enter either 1 - 2 - 3 \n")

    def volume(self):
        print("\n **** Volume **** \n")

        while True:
            try:
                global calculate
                volume = int(input(
                    "Choose what you want to calculate :\n Enter 1. Volume of Cube \n Enter 2. Volume Of Cylinder  \n Enter 3. Volume of Sphere \n Enter 0. To Exit : "))
                if(volume == 1):
                    side = float(input("Enter Side Of cube : "))
                    calculate = side ** 3
                    return calculate
                elif(volume == 2):
                    radius = float(input("Enter Radius Of Cylinder : "))
                    height = float(input("Enter height Of Cylinder : "))
                    calculate = 3.14 * radius ** 2 * height
                    return calculate
                elif(volume == 3):
                    radius = float(input("Enter Radius Of Sphere : "))
                    calculate = (4/3) * 3.14 * radius**3
                    return calculate
                elif(volume == 0):
                    return "Thanks For Using This Program"
                else:
                    raise TypeError
            except TypeError:
                print("You entered wrong Input. Please Try again.\n")
            except ValueError:
                print(
                    f"Invalid choice: {volume}  Please enter either 1 - 2 - 3 \n")
