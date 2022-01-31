#!/usr/bin/python3
"""
Module area and __str__
"""


Rectangle = __import__('9-rectangle').Rectangle
"""
Rectangle class
"""


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size):
        """
        Initializes values
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates area
        """
        return (self.__size * self.__size)

    def __str__(self):
        """
        Prints square description
        """
        return("[Square] {}/{}".format(self.__size, self.__size))
