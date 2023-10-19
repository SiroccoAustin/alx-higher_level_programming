#!/usr/bin/python3
"""Base module for managing IDs in the project."""
import json


class Base:
    """Base class for managing IDs in other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.

        Args:
            id (int, optional): The ID to assign to the instance. If not provided, a new ID will be generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a json string made out of the dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the list of objects to a file"""
        from .rectangle import Rectangle
        from .square import Square
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
        """decodes json string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance of class"""
        from .rectangle import Rectangle
        from .square import Square
        if cls is Rectangle:
            new_instance = Rectangle(1, 1, 0, 0, 0)
            new_instance.update(**dictionary)
            return new_instance
        elif cls is Square:
            new_square = Square(3, 0, 0, 0)
            new_square.update(**dictionary)
            return new_square