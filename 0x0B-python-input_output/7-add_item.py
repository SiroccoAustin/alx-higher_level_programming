#!/usr/bin/python3
"""Save arguments"""
import sys
import json
savejson = __import__("7-save_to_json_file").save_to_json_file
loadjson = __import__("8-load_from_json_file").load_from_json_file

try:
    Array = loadjson("add_item.json")
except FileExistsError:
    Array = []
arguments = sys.argv[1:]

for argument in arguments:
    Array.append(argument)
savejson(Array, "add_item.json")