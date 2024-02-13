#!/usr/bin/python3
"""square class that inherits from Rectangle class"""
from models.rectangle import Rectangle
from inspect import classify_class_attrs


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor- calls super class using logic for Rectangle __init__
        """
        super().__init__(size, size, x, y,  id)

    def __str__(self):
        """__str__function"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))

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
                if list_attr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)
    def to_dictionary(self):
        """public method that returns the dictionary"""
        dict1 = self.__dict__
        dict2 = {}
        dict2['id'] = dict1['id']
        dict2['size'] = dict1['_Rectangle__width']
        dict2['x'] = dict1['_Rectangle__x']
        dict2['y'] = dict1['_Rectangle__y']
        return (dict2)
