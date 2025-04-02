#!/usr/bin/python3


def add_integer(a, b=98):
    """ Adds two integers or floats. If any input is a float, it is casted int
    o an integer. """


    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
