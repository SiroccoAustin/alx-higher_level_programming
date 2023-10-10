#!/usr/bin/python3
"""Save arguments"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    Array = load_from_json_file("add_item.json")
except FileNotFoundError:
    Array = []

Array.extend(sys.argv[1:])
save_to_json_file(Array, "add_item.json")