"""
Create a Python Unit Convertor

"""


# Convert Miles to Kilometers

def print_menu():
    print('1. Km to Miles')
    print('2. Miles to Km')


def km_miles():
    km = float(input("Enter the distance in Km: "))
    miles = km / 1.609
    print("Distance in Miles: {0}".format(miles))


def miles_km():
    miles = float(input("Enter the distance in Miles: "))
    km = miles * 1.609
    print("Distance in km: {0}".format(km))


if __name__ == '__main__':
    print_menu()
    userInput = input("Choose your conversion: ")
    if userInput == '1':
        km_miles()
    if userInput == '2':
        miles_km()