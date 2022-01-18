#!/usr/bin/python3
"""
Square module - provides a class Square with initialized size or 0 default
Raises errors for invalid input
Getters and Setters for size
Calculates square area
"""


class Square:
    """
    Defines a square by initialized size or 0 default and can compute area
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
