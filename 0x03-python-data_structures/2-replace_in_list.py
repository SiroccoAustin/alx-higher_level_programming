#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= range(len(my_list)):
        return my_list
    else:
        my_list[idx] = element
        return my_list
