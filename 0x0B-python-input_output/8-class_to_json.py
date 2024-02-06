#!/usr/bin/python3
"""Module containing the function class to json"""


def class_to_json(obj):
    """Returns a dictionary description with simple data structure,
    """
    return obj.__dict__
