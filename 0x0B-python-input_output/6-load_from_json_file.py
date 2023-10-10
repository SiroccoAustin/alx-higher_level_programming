#!/usr/bin/python3
"""Function that load json file"""
import json

def load_from_json_file(filename):
    """unload json file"""
    with open(filename, "r") as file:
        return json.load(file)