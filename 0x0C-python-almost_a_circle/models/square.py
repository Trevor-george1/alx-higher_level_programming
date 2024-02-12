#!/usr/bin/python3
"""square class that inherits from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """constructor- calls super class using logic for Rectangle __init__
        """
        super().__init__(size, size, x, y,  id)

    def __str__(self):
        """__str__function"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """Property retriever for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Property setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """public method"""
        if args is not None and len(args) is not 0:
            list_attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)