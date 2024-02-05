#!/usr/bin/python3
"""function that checks if obj is alist or subclass of class"""


def is_kind_of_class(obj, a_class):
    """returns True if isinstance of list or issubclass of a_class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
