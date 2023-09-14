#!/usr/bin/python3

def best_score(a_dictionary):
    high_score = None
    for key, value in a_dictionary.items():
        if high_score in None or value > high_score:
            high_score = value
    return high_score