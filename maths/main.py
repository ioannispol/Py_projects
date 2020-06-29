"""
Ioannis Polymenis

Main script to calculate the Area of shapes
There are six different shapes:
    - square
    - rectangle
    - triangle
    - circle
    - rhombus
    - trapezoid

"""
import os
import class_area as ca

while True:
    os.system('cls')

    print("*" * 30)
    print("Welcome to Area Calculator ")
    print("Options:")
    print("s = Square")
    print("r = Rectangle")
    print("tri = Triangle")
    print("c = Circle")
    print("rh = Rhombus")
    print("trap = Trapezoid")
    print("q = Quit")
    print("*" * 30)

    userInput = input("Enter the shape command: ")
    if userInput == 's':
        width = int(input("Enter the width of square: "))
        height = int(input("Enter the height of the square: "))
        square = ca.Area(width, height)
        print("Square area: %d" % (square.square_area()))
    elif userInput == 'r':
        width = int(input("Enter the width of square: "))
        height = int(input("Enter the height of the square: "))
        rectangle = ca.Area(width, height)
        print("Rectangle area: %d" % (square.rectangle_area()))
    elif userInput == 'tri':
        base = int(input("Enter base of the triangle: "))
        tri_height = int(input("Enter height of the triangle: "))
        tri = ca.Triangle(base, tri_height)
        print("Triangle Area: %d" % (tri.area()))
    elif userInput == 'c':
        radius = int(input("Enter circle radius: "))
        cir = ca.Circle(radius)
        print("Circle area: %d" % cir.area())
    elif userInput == 'rh':
        width = int(input("Enter the width of rhombus: "))
        height = int(input("Enter the height of the rhombus: "))
        rh = ca.Rhombus(width, height)
        print("Rhombus area: %d" % (rh.area()))
    elif userInput == 'trap':
        base = int(input("Enter the base of the trapezoid: "))
        base2 = int(input("Enter the 2nd base of the trapezoid: "))
        height = int(input("Enter the height of the trapezoid: "))
        trap = ca.Trapezoid(base, base2, height)
        print("Trapezoid area: %d" % (trap.area()))
    elif userInput == 'q':
        break
