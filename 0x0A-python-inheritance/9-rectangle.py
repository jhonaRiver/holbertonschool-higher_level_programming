#!/usr/bin/python3
"""
Module area __str__
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Class BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    Class Rectangle
    """
    def __init__(self, width, height):
        """
        initializes values
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates area
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Prints Rectangle description
        """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
