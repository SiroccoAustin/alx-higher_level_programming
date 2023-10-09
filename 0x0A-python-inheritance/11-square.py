#!/usr/bin/python3

"""Defines the square class which inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle

"""Square Class"""

class Square(Rectangle):
    """Class defining a square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__Rectangle__width, self.__Rectangle__height)