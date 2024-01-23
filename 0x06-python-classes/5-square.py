#!/usr/bin/python3
"""create a class Square"""


class Square:
    """Init the square"""
    def __init__(self, size=0):
        self.__size = size
    """create a property - size"""
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

    """public method that returns square area"""
    def area(self):
        return self.__size ** 2

    """ public method that prints the square"""
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
