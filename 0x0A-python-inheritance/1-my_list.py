#!/usr/bin/python3

"""Class that inherits from list"""

class MyList(list):
    def print_sorted(self):
        """Function that prints a sorted list"""
        print(sorted(self))