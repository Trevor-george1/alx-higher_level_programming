#!/usr/bin/python3
"""creates a class Square"""


class Square:
    """Initlaize the square"""
    def __init__(self, size=0):
        self.__size = size

    """public method that gets area of square"""
    def area(self):
        result = self.__size * self.__size
        return result
    """ create a property size"""
    @property
    def size(self):
        return self.__size

    """create a setter"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
