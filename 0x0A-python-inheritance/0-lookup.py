#!/usr/bin/python3

"""Write a function that prints all the class attributes"""

def lookup(obj):
    """function that prints all the attributes"""
    attributes = dir(obj)
    return attributes