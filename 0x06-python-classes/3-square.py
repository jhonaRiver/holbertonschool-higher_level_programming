#!/usr/bin/python3
"""
Module Square - provides a class Square with initialized size or 0 default
Raises errors for invalid input
Calculates the square area
"""


class Square:
    """
    Defines a square with initialized size or 0 default
    Raises errors for invalid input
    Calculates square area
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
