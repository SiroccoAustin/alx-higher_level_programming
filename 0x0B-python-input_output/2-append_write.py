#!/usr/bin/python3

"""Function that appends to a file"""

def append_write(filename="", text=""):
    """function to append"""
    with open(filename, "a") as file:
        return file.write(text)