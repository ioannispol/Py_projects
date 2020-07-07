"""
Set Length functions

"""


def km():
    """Convert Km to Miles"""
    value = float(input("Enter the value in km: "))
    conversion = value / 1.609
    return "{0} Km is {1:.3f} Miles".format(value, conversion)


def miles():
    """Convert Miles to Km"""
    value = float(input("Enter the value in miles: "))
    conversion = value * 1.609
    return "{0} Miles is {1:.3f} Km".format(value, conversion)


def n_miles():
    """Convert Nautical miles to Km"""
    value = float(input("Enter the value in nautical miles: "))
    conversion = value * 1.852
    return "{0} Nautical Miles is {1:.3f} Km".format(value, conversion)


def m_cm():
    """Convert meters to centimetres"""
    from math import exp
    value = float(input("Enter the length in meters: "))
    conversion = value * exp()


def cm_inch():
    value = float(input("Enter the centimeters: "))
    conversion = value * 0.39370
    return "{0} cm is {1:.2f} inches".format(value, conversion)
