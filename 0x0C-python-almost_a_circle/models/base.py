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