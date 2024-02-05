#!/usr/bin/python3
"""class rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """constructor"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    """area"""
    def area(self):
        return self.__width * self.__height
    """__str__"""
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)