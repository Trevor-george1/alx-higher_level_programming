#!/usr/bin/python3
"""program that creates Base class"""


class Base:
    """"private attribute"""
    __nb_objects = 0
    """constructor"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects