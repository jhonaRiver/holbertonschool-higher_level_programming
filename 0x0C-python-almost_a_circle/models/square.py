#!/usr/bin/python3
"""
Module Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Prints Square info
        """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'\
               .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Getter size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns arguments to each attribute
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'size', 'x', 'y']
        if argc > 4:
            argc = 4
        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        Dictionary representation of Square
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
