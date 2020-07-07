""" Python Calculus calculator"""

import math
import sympy
from sympy import Symbol, Derivative


# create a simple function

def f(x):
    return x ** 2


f(4)
print(f(4))


# Define a derivative

def der(f, v):
    h = 0.00000000001
    top = f(v + h) - f(v)
    bottom = h
    slope = top / bottom
    return float("%.3f" % slope)


print(der(f, 16))

t = Symbol('t')
St = 5 * t ** 2 + 2 * t + 8
Derivative(St, t)
