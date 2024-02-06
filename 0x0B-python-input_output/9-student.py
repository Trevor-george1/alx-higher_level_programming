#!/usr/bin/python3
"""class that defines a student"""


class Student:
    """constructor"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """method to_json"""
    def to_json(self):
        return self.__dict__
