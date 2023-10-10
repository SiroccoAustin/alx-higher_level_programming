#!/usr/bin/python3
"""Function that load json file"""
import json

def load_from_json_file(filename):
    with open(filename, "r") as file:
        json.loads(file)