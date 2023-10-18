#!/usr/bin/python3
"""Defines a rectangle class."""
from base import Base



class Rectangle(Base):
    """Class for drawing a Rectangle"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width: width of the Rectangle
            height: height of the Rectangle
            x: spaces
            y: spaces
            id (int, optional): The ID to assign to the instance. If not provided, a new ID will be generated.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)