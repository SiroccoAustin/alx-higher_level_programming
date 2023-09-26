#!/usr/bin/python3

"""defining a class"""

class Square:
    """Creating a class that define size"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    
    def area(self):
        """calculates the area"""
        return self.__size * self.__size
    
    def size(self):
        """getter"""
        return self.__self.size
    
    def size(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
