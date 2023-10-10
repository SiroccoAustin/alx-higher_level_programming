#!/usr/bin/python3
"""Function that return a dict"""

def class_to_json(obj):
    """"class to json function"""
    class_dict = {}
    convert_to_dict = obj.__dict__
    for elem in convert_to_dict:
        if type(elem) in [list, bool, str, dict, int]:
            class_dict[elem] = convert_to_dict[elem]
    return class_dict