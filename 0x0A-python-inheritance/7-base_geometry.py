#!/usr/bin/python3

"""BaseGeometry Class"""

class BaseGeometry:
    """Define a base geometry class"""
    def area(self):
        """Calculates the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates whether values is an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))