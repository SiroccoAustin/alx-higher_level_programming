#!/usr/bin/python3

"""Class that inherits from list"""

class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Function that prints a sorted list"""
        print(sorted(self))