#!/usr/bin/python3
"""
Module __init__
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
