#/usr/bin/python3
"""function that checksif an objct is an
instance of a class directly or indirect"""


def inherits_from(obj, a_class):
    """Returns True or False"""
    return isinstance(obj, a_class) and type(obj) != a_class
