#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    First_letter = sentence[0] if sentence else None
    new_tuple = (length, First_letter)
    return new_tuple
