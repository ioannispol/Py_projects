import os
import math
from __future__ import division


def main_menu():
    print("1. Length")
    print("2. Temperature")
    print("q to quit")


def length_menu():
    print("1. From Km to Miles")
    print("2. From Miles to Km")


def temp_menu():
    print("1. From Celsius to Kelvin")
    print("2. From Kelvin to Celsius")


class Length(object):

    def __init__(self):


    def km_miles(self, km):
        self.km = km
        miles = self.km / self.constant
        print("Distance in Miles: {0}".format(miles))
        return km_miles

    def miles_km(self, miles):
        miles = float(input("Enter the distance in Miles: "))
        km = miles * self.constant
        print("Distance in Km: {0)".format(km))
        return miles_km



while True:
    os.system('cls')
    main_menu()

    userInput = input("Choose an option from the main menu:")
    if userInput == '1':
        pass
    elif userInput == '2':
        length_menu()
        userInput = input("Choose the length conversion: ")
        if userInput == '1':

