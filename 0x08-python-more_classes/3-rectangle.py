#!/usr/bin/python3
"""class that defines a class Rectangle"""


class Rectangle:
    """initialize the class"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    """height property"""
    @property
    def height(self):
        return self.__height

    """height setter"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    """width property """
    @property
    def width(self):
        return self.__width
    """width setter"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    """public instance method area"""
    def area(self):
        result = self.__height * self.__width
        return result
    """public instance method perimeter"""
    def perimeter(self):
        per = 2 * (self.__width + self.__height)
        return per
    """str method"""
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for _ in range(self.__height):
                rectangle_str += '#' * self.__width + '\n'
            return rectangle_str[:-1]
