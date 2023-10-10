#!/usr/bin/python3
"""Function that writes an object to a file"""
import json

def save_to_json_file(my_obj, filename):
    """write object to file"""
    with open(filename, "w") as file:
        json.dumps(my_obj, file)