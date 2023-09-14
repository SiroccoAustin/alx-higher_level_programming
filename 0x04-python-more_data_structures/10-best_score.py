#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    high_score = None
    max_value = float("-inf")
    for key, value in a_dictionary.items():
        if value > high_score:
            high_score = value
            max_value = value
    return high_score