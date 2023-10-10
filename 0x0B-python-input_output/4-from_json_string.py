#!/usr/bin/python3
"""function to decode json data"""
import json

def from_json_string(my_str):
    """function to decode json data"""
    return json.loads(my_str)