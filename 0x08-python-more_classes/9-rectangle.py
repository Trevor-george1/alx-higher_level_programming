#!/usr/bin/python3
"""class Rectangle uses __repr__, __str__"""


class Rectangle:
    """
    number of instances
    """
    number_of_instances = 0
    """
        print_symbol #
    """
    print_symbol = '#'
    """Initialize the recatngle"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1
    """
        property (width)
    """
    @property
    def width(self):
        return self.width
    """
        width property setter
    """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("Width must be  >= 0")
        self.__width = value
    """
        property (height)
    """
    @property
    def height(self):
        return self.__height
    """
        height  property setter
    """
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height
    """
        Method area
        - returns the area of the rectangle
    """
    def area(self):
        return self.__height * self.__width
    """
        Perimeter
        - returns the perimeter of the rectangle
    """
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height * self.__width)
    """
        __str__
        print the rectangle using #
        - width < 0 or heigth < 0 return 0
    """
    def __str__(self):
        new_string = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            for _ in range(self.__height):
                new_string += str(self.print_symbol) * self.__width + '\n'
            return new_string[:-1]
    """
        __repr__
        return a string representaion of rectangle
    """
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
    """
        __del__
        prints a message when a recatngle is deleted
    """
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    """
        bigger_or_equal - returns biggest rectangle based on area
    """
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
    """
        square(cls, size=0) - retuns a new Rectangle instance
        with heigth == width, size
    """
    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
