#!/usr/bin/python3
"""creates a class Square"""


class Square:

    """init the Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """property called size"""

    @property
    def size(self):
        return self.__size

    """setter property for size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """property called position"""
    @property
    def position(self):
        return self.__position

    """setter for position"""
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) and not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    """ public method area"""
    def area(self):
        return self.__size ** 2

    """public method print"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                print("#" * (self.__size))
