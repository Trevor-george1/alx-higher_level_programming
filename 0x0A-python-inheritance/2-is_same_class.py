#!/usr/bin/python3
"""function that checks if object is an instance of specified class"""


def is_same_class(obj, a_class):
    """fucntion that returns True if object is exactly
        instance of a_class
    """
    return type(obj) == a_class
