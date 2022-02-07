#!/usr/bin/python3
"""
Module Rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """
    Defines Rectangle class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor
        """
        super().__init__(id)
        self.check_integer_parameter(width, 'width')
        self.check_integer_parameter(height, 'height')
        self.check_integer_parameter(x, 'x')
        self.check_integer_parameter(y, 'y')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter width
        """
        self.check_integer_parameter(value, 'width')
        self.__width = value

    @property
    def height(self):
        """
        Getter height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter height
        """
        self.check_integer_parameter(value, 'height')
        self.__height = value

    @property
    def x(self):
        """
        Getter x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter x
        """
        self.check_integer_parameter(value, 'x')
        self.__x = value

    @property
    def y(self):
        """
        Getter y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter y
        """
        self.check_integer_parameter(value, 'y')
        self.__y = value

    def check_integer_parameter(self, value, param):
        """
        Validation of values
        """
        if type(value) is not int:
            raise TypeError(param + ' must be an integer')
        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')
        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')
