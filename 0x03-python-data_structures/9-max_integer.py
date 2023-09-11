#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    i = 0
    num = my_list[0]
    while i < len(my_list):
        if my_list[i] > num:
            num = my_list[i]
        i += 1
    return num
