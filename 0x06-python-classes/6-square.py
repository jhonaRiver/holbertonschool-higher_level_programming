#!/usr/bin/python3
"""
Square module - provides a class Square with initialized size or 0 default
Initialized position or (0, 0) default
Raises errors for invalid input
Setters and getters for size and position
Calculates area of square
Prints square with #
"""


class Square:
    """
    Defines a square with initialized size and position or 0 default
    calculates area and prints square with #
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) != tuple or len(position) != 2 or not all([type(i)
           == int for i in position]) or not all([i >= 0 for i in position]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
