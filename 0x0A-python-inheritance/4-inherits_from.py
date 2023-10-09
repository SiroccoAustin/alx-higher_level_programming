#!/usr/bin/python3

"""Function that checks if an instance inherits from class"""

def inherits_from(obj, a_class):
    """inherit from class"""
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)