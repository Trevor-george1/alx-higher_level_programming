#!/usr/bin/python3
"""program that creates Base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns  json representation of list dictionaries"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        """writes the json string to a file"""
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            list_dic.append(list_objs.to_dictionary())
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)
