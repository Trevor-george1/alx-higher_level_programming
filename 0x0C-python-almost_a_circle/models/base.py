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

    def to_json_string(list_dictionaries):
        """returns  json representation of list dictionaries"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dump(list_dictionaries)
