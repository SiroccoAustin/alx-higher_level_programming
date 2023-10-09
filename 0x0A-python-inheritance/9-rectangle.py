#!/usr/bin/python3

"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Define Rectangle class"""
        
class Rectangle(BaseGeometry):
    """Define Rectangle class"""
    def __init__(self, width, height):
        """initialize private variables"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        """Define area of the Rectangle"""
        return self.__width * self.__height
    
    def __str__(self):
        """returns a string to print"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

