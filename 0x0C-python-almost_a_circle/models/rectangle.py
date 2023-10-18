#!/usr/bin/python3
"""Defines a rectangle class."""
from .base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width
    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height
    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("width must be an integer")
        if height < 1:
            raise ValueError("width must be > 0")
        self.height = height
    @property
    def x(self):
        """Set/get the x coordinates of the Rectangle."""
        return self.__x
    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("width must be an integer")
        if x < 1:
            raise ValueError("width must be > 0")
        self.__x = x
    @property
    def y(self):
        """Set/get the y coordinates of the Rectangle."""
        return self.__y
    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("width must be an integer")
        if y < 1:
            raise ValueError("width must be > 0")
        self.__y = y

    