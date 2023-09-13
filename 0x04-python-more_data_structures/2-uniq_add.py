#!/usr/bin/python3

def uniq_add(my_list=[]):
    filter_duplicates = []
    result = 0
    for i in my_list:
        if i not in filter_duplicates:
            filter_duplicates.append(i)
    for item in filter_duplicates:
        result += item
    return result