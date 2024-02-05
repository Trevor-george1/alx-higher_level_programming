#!/usr/bin/python3
"""function that returns a list of available attributes
    and method of an object
"""


def lookup(obj):
    """
        returns a list of attributes and methods
    """
    return dir(obj)
