#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    num = len(my_list)
    while num > 0:
        num -= 1
        print(my_list[num])
