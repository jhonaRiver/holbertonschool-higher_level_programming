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

    def area(self):
        """
        Calculates area
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the rectangle in STDOUT
        """
        if self.__y > 0:
            print('\n' * self.__y, end='')
        for i in range(self.__height):
            if self.__x > 0:
                print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """
        Prints Rectangle info
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'\
                .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Assigns arguments to each attribute
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'width', 'height', 'x', 'y']
        if argc > 5:
            argc = 5
        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        Dictionary representation of Rectangle
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
