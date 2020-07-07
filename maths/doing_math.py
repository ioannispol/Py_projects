"""
    Animate the trajectory of an object in projectile motion

"""
from matplotlib import pyplot as plt
from matplotlib import animation
import math

g = 9.81


def get_intervals(u, theta):
    t_flight = 2 * u * math.sin(theta) / g
    intervals = []
    start = 0
    interval = 0.005
    while start < t_flight:
        intervals.append(start)
        start = start + interval
    return intervals


def update_position(i, circle, intervals, u, theta):
    t = intervals[i]
    x = u * math.cos(theta) * t
    y = u * math.sin(theta) * t - 0.5 * g * t * t
    circle.center = x, y
    return circle,


def create_animation(u, theta):
    intervals = get_intervals(u, theta)
    xmin = 0
    xmax = u * math.cos(theta) * intervals[-1]
    ymin = 0
    t_max = u * math.sin(theta) / g
    ymax = u * math.sin(theta) * t_max - 0.5 * g * t_max ** 2
    fig = plt.gcf()
    ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))

    circle = plt.Circle((xmin, ymin), 1.0)
    ax.add_patch(circle)

    anim = animation.FuncAnimation(fig, update_position,
                                   fargs=(circle, intervals, u, theta),
                                   frames=len(intervals), interval=1,
                                   repeat=False)

    plt.title("Projectile Motion")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


if __name__ == '__main__':
    try:
        u = float(input("Enter the initial velocity (m/s): "))
        theta = float(input("Enter the angle of projectile (degrees): "))
    except ValueError:
        print("You entered an invalid input")
    else:
        theta = math.radians(theta)
        create_animation(u, theta)

"""Derivative calculator"""

from sympy import Symbol, Derivative, sympify, pprint
from sympy.core.sympify import SympifyError


def derivative(f, var):
    var = Symbol(var)
    d = Derivative(f, var).doit()
    pprint(d)


if __name__ == '__main__':
    f = input("Enter a function: ")
    var = input("Enter the variable to differenciate with respect to: ")
    try:
        f = sympify(f)
    except SympifyError:
        print("Invalid input")
    else:
        derivative(f, var)
