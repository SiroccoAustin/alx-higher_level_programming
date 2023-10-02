#!/usr/bin/python3

"""Creating a Rectangle Class"""

class Rectangle:
    """Initialize Rectangle Class"""
    def __init__(self, width=0, height=0):
        """Initailizing Variables"""
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """getter"""
        return self.__width
    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height
    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """Calculate Area"""
        return self.__width * self.__height
    def perimeter(self):
        """Calculate the Perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (self.__width * 2) + (self.__height * 2)



    