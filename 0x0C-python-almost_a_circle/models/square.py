#!/usr/bin/python3
"""Defines a rectangle class."""
from .rectangle import Rectangle

class Square(Rectangle):
    """Represent a sqaure."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates Rectangle attributes. In the following order if positional:
        id, width, height, x, y
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
            self.height = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        if len(args) == 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)