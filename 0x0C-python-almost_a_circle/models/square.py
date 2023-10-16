#!/usr/bin/python3

from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, size, size)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        return self.width
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
    def update(self, *args, **kwargs):
        numargs = len(args)
        if numargs > 0:
            self.id = args[0]
        if numargs > 1:
            self.width = args[1]
            self.height = args[1]
        if numargs > 2:
            self.x = args[2]
        if numargs > 3:
            self.y = args[3]
        if numargs == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
    
    def to_dictionary(self):
        new_dict = {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
        return new_dict