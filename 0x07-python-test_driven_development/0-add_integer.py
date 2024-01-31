#!/usr/bin/python3
'''
    function that adds two numbers
    raise exception if numbers are not integers or float
'''


def add_integer(a, b=98):
    """
        add numbers and returns sum
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
