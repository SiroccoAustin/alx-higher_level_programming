#!/usr/bin/python3

"""Function to write to a file"""

def write_file(filename="", text=""):
    """Write file function"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)