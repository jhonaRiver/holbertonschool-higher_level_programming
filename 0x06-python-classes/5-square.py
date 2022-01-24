#!/usr/bin/python3
"""
Square module - provides a class Square with initialized size or 0 default
Raises errors for invalid input
Calculates square area
Getters and setters for size
Prints the square with #
"""


class Square:
    """
    Defines a square with initialized size or 0 default, can compute area and
    print the square using #
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

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)