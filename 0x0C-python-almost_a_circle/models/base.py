#!/usr/bin/python3
"""
Module Base class
"""

from os import path
import json


class Base:
    """
    Defines class Base to manage the id attribute of all classes that extend from it and avoid duplicates
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
