#!/usr/bin/python3
"""class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """constructor"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
    """area"""
    def area(self):
        return self.__size * self.__size
    """__str__"""
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
