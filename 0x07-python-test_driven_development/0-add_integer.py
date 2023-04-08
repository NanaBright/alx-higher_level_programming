#!/usr/bin/python3

def add_integer(a, b=98):
    """ Check if a and b are integers or floats """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    """ Cast a and b to integers if they are floats """
    if isinstance(a, float):
        a = int(a)
        if isinstance(b, float):
            b = int(b)

    """ Perform the addition """
    result = a + b

    """ Return the result as an integer """
    return int(result)
