#!/usr/bin/python3
"""Base geometry class"""


class BaseGeometry:
    """method area"""
    def area(self):
        """raise Exception"""
        raise Exception("area() is not implemented")
    """method integer_validator"""
    def integer_validator(self, name, value):
        """validates the value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
