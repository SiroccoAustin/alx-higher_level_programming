#!/usr/bin/python3
import json

"""defining Base class"""

class Base:
    """Base geometry class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = Base.__nb_objects
            Base.__nb_object += 1
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        from rectangle import Rectangle
        from square import Square
        list_copy = list_objs.copy()
        for i in range(len(list_copy)):
            list_copy[i] = list_copy[i].to_dictionary()
        if cls is Rectangle:
            with open("Rectangle.json", "w") as file:
                file.write(Base.to_json_string(list_copy))
        elif cls is Square:
            with open("Square.json", "w") as file:
                file.write(Base.to_json_string(list_copy))
    
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        from rectangle import Rectangle
        from square import Square
        if cls is Rectangle:
            new_class = Rectangle(4, 2, 4, 1, 3)
            new_class.update(**dictionary)
            return new_class
        elif cls is Square:
            new_cls = Square(4, 4, 0, 0, 0)
            new_cls.update(**dictionary)
            return new_cls
    @classmethod
    def load_from_file(cls):
        from rectangle import Rectangle
        from square import Square

        if cls is Rectangle:
            with open("Rectangle.json", "r") as file:
                readlist = Base.from_json_string(file.read())
                if readlist == "":
                    return []
                for i in range(len(readlist)):
                    readlist[i] = Rectangle.create(**readlist[i])
            return readlist
        elif cls is Square:
            with open("Square.json", "r") as file:
                sqrlist = Base.from_json_string(file.read())
                if sqrlist == "":
                    return []
                for i in range(len(sqrlist)):
                    sqrlist[i] = Rectangle.create(**sqrlist[i])
            return sqrlist
