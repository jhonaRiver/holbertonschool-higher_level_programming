#!/usr/bin/python3
"""
Square module - provides a class Square with initialized value or 0 default
Raises errors for invalid input
"""


class Square:
    """
    Defines a square with initialized value or 0 default
    Raises errors for invalid input
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
