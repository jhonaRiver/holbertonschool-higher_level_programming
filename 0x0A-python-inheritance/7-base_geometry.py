#!/usr/bin/python3
"""
area and integer_validator module
"""


class BaseGeometry:
    """
    Class BaseGeometry
    """
    def area(self):
        """
        Raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if its an integer
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
