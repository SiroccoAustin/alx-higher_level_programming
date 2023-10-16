#!/usr/bin/python3
from base import Base
"""Define the Rectangle class"""

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init(id)
    
    @property
    def width(self):
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
        return self.__y
    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("width must be an integer")
        if y < 1:
            raise ValueError("width must be > 0")
        self.__y = y
    
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def area(self):
        """Returns area of Rectangle"""
        return self.__height * self.__height

    def display(self):
        """Display the Rectangle in the console"""
        string = "#"
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.x, end="")
            print(string * self.__width)

    def update(self, *args, **kwargs):
        """update method"""
        numargs = len(args)
        if numargs > 0:
            self.id = args[0]
        if numargs > 1:
            self.width = args[1]
        if numargs > 2:
            self.height = args[2]
        if numargs > 3:
            self.x = args[3]
        if numargs > 4:
            self.y = args[4]
        if numargs == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        new_dict = {"id": self.id, "width": self.width, "height": self.height,
                   "x": self.x, "y": self.y}
        return new_dict