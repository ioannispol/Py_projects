"""
    A trigonometry calculator using Python

"""

import math as mt
import os


def right_angle():
    """Use Pythoagorian theorem to calculate, angles and sides of the triangle"""

    while True:
        os.system('cls')

        print("*" * 40)
        print("To calculate the Hypotenuse type 'hyp': ")
        print("To calculate the Opposite type 'opo':")
        print("To calculate the Adjacent type 'adj': ")
        print("To exit type 'q': ")
        print("*" * 40)

        userInput = (str((input("Enter your option: ")))).lower()

        # Calculate the hypotenuse of the triangle
        # Todo: Make an integration and use the first user input to feed other options!
        if userInput == 'hyp':
            degrees = float(input("Enter the angle in degrees: "))
            opposite = float(input("Enter the value of the opposite: "))
            result = float(opposite * mt.sin(degrees))
            print("The value of the Hypotenuse is: {:.3}".format(result))
        elif userInput == 'opo':
            degrees = float(input("Enter the angle in degrees: "))
            hypotenuse = float(input("Enter the value of hypotenuse: "))
            result = float(hypotenuse * mt.sin(degrees))
            print(" The value of the Opposite is: {:.3}".format(result))
        elif userInput == 'adj':
            print("What are your data? Hypotenuse or Opposite? ")
            data = str(input("For Hypotenuse type 'hyp' and Opposite type 'opo': "))
            if data == 'hyp':
                hypotenuse = float(input("Enter the value of hypotenuse: "))
                theta = float(input("Enter the angle in degrees: "))
                result = hypotenuse * mt.cos(theta)
                print("The value of Adjacent is: {:.3}".format(result))
            elif data == 'opo':
                opposite = float(input("Enter the value of the opposite: "))
                theta = float(input("Enter the angle in degrees: "))
                result = abs(opposite / mt.tan(theta))
                print("The value of Adjacent is: {:.3}".format(result))
            else:
                break

        elif userInput == 'q':
            break
        else:
            print("Invalid input!! Please try again")
            print("Press Enter to quit")

    return right_angle()


right_angle()

# Todo: create more options for trigonometry calculations
