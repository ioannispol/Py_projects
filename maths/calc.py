""""
Author: Iaonnis Polymenis
PyCalc - Python Calculator

"""
import math as mt
import os
import class_simple as cs


def calculator():
    """A function for simple calculations
        - Addition
        - Subtraction
        - Multiplication
        - Division
    """

    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    calc = cs.Calculations(x, y)

    while True:

        # os.system('cls')

        def menu():
            a = '1. Add\n2. Sub\n3. Multiply\n4. Divide'
            print("*" * 40 + "\nWelcome to PyCalc\n" + a + "\n" + "*" * 40)
        menu()

        userInput = (int((input("Enter your option: "))))

        #userInput = 1

        if userInput == 1:
            print("Result: ", calc.add())
        elif userInput == 2:
            print("Result: ", calc.sub())
        elif userInput == 3:
            print("Result: ", calc.mult())
        elif userInput == 4:
            print("Result: ", calc.div())
        elif userInput == 0:
            print("Invalid choice. Please try again!!!")
            break

    return calculator()


calculator()
