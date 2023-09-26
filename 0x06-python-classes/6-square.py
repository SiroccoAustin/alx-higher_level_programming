#!/usr/bin/python3

"""defining a class"""


class Square:
    """Creating a class that define size"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not (isinstance(position, tuple) and
                len(position) == 2 and
                all(isinstance(x, int) and x >= 0 for x in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position
    
    
    def area(self):
        """calculates the area"""
        return self.__size * self.__size
    
    @property
    def size(self):
        """getter"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position getter"""
        return self.__position
    
    @position.setter
    def position(self, value):
        """position setter"""
        if not (isinstance(value, tuple) and
                len(value) == 2 and
                all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """print # in range of size"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            hash = "#" * self.__size
            pos = ' ' * self.__position[0]
            for _ in range(self.__size):
                print(pos + hash)