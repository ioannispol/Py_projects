"""class UnitConvert:
    def __init__(self, metric, imperial):
        self.metric = metric
        self.imperial = imperial

    def get_menu(self):
        print("1. For SI units")
        print("2. For Imperial units ")
        return self.get_menu()
"""
import os





class Length:
    def __init__(self, conv):
        self.conv = conv

    def km_miles(self):
        result = float(self.conv / 1.609)
        return result

    def miles_km(self):
        result = float(self.conv * 1.609)
        return result


class Mass:
    pass


class Pressure:
    def __init__(self, conv):
        self.conv = conv

    def pascal(self):
        result = float(self.conv * 1.0e-5)
        return result

    def bar(self):
        result = float(self.conv * 1.0e5)
        return result


class Temperature:
    """C = K - 273.15
    K = C + 273.15"""

    class Unit():
        K = 'K'
        C = 'C'
        R = 'R'
        F = 'F'

    def __init__(self, conv):
        self.conv = conv

    def kelvin(self):
        c = float(self.conv - 273.15)
        return c

    def celsius(self):
        k = float(self.conv + 273.15)
        return k

    def fahrenheit(self, c, f):
        """Convert from Celsius to Fahrenheit
        F = 9/5 * C + 32
        C = 5/9 * (F - 32)
        """

        return self.fahrenheit


class Energy:
    pass


def temp_menu():
    while True:
        os.system('cls')
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("q to exit")

        user_input = input("Coose Celsius or Fahrenheit: ")
        if user_input == '1':
            c = float(input("Enter the temperature in Celsius: "))
            f = 9 / 5 * c + 32
            print("{0} Celsius is {1} Fahrenheit".format(c, f))
        elif user_input == '2':
            f = float(input("Enter the temperature in Fahrenheit: "))
            c = 5 / 9 * (f - 32)
            print("{0} Fahrenheit is {1} Celsius".format(f, c))
        elif user_input == 'q':
            break

    return temp_menu


def main():
    os.system('cls')
    print("1. Km to Miles")
    print("2. Miles to Km")
    print("3. Pascal to Bar")
    print("4. Bar to Pascal")
    print("5. Kelvin to Celsius")
    print("6. Celsius to Kelvin")
    print("7. Other temps")

    userInput = input("Choose the conversion: ")

    if userInput == '1':
        value = float(input("Enter the distance in kilometers: "))
        km_miles = Length(value)
        print(km_miles.km_miles())
    elif userInput == '2':
        value = float(input("Enter the distance in miles: "))
        miles_km = Length(value)
        print(miles_km.miles_km())
    elif userInput == '3':
        value = float(input("Enter Pressure in Pascal: "))
        bar = Pressure(value)
        result = bar.pascal()
        print("{0} pascal is {1:.4f}0 bar".format(value, result))
    elif userInput == '4':
        value = float(input("Enter Pressure in Bar: "))
        bar = Pressure(value)
        result = bar.bar()
        print("{0} bar is {1}0 pascal".format(value, result))  # Todo: to print KPa or MPa
    elif userInput == '5':
        value = float(input("Enter the temperature in Kelvin: "))
        c = Temperature(value)
        result = c.kelvin()
        print("{0} Kelvin is {1:.2f} Celsius".format(value, result))
    elif userInput == '7':
        print("Choose the conversion")


if __name__ == '__main__':
    main()
