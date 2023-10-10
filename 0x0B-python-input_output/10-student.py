#!/usr/bin/python3

"""Class that defines a student"""

class Student:
    """define a student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """convert to dict"""
        if type(attrs) is list:
            for elem in attrs:
                if type(elem) is not str:
                    break
        dict_return = {}
        convert_to_dict = self.__dict__
        for elem in convert_to_dict:
            if type(convert_to_dict[elem]) in [bool, int, dict, str, list]:
                dict_return[elem] = convert_to_dict[elem]
        return dict_return