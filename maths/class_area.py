class Area(object):
    """
    Writing a simple python calculator using Classes

    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square_area(self):
        return self.width * self.height

    def rectangle_area(self):
        return self.width * self.height


class Triangle(Area):

    def __init__(self, base, tri_height):
        self.base = base
        self.tri_height = tri_height

    def area(self):
        """ tri_area = (base * height) / 2"""
        return (self.base * self.tri_height) / 2


class Circle(Area):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        from math import pi
        return pi * self.radius ** 2


class Rhombus(Area):
    def __init__(self, width, height):
        super().__init__(width, height)

    def area(self):
        return (self.width * self.height) / 2


class Trapezoid(Area):
    def __init__(self, base, base2, height):
        self.base = base
        self.base2 = base2
        self.height = height

    def area(self):
        return ((self.base + self.base2) * self.height) / 2
