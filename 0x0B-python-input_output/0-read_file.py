#!/usr/bin/python3

"""Function that reads file"""

def read_file(filename=""):
    """read file function"""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")