#!/usr/bin/python3
"""Class that defines a Square using exceptions"""


class Square:
    """initialization of class Square with size"""
    def __init__(self, size=0):
        """use exception to check validity of size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
