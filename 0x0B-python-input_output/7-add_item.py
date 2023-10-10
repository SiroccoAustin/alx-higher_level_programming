#!/usr/bin/python3
"""Save arguments"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    Array = load_from_json_file("add_item.json")
except FileNotFoundError:
    Array = []
arguments = sys.argv[1:]
Array.extend(arguments)
save_to_json_file(Array, "add_item.json")