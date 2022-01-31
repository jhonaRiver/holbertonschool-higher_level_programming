#!/usr/bin/python3
"""
lookup module
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    """
    list = dir(obj)
    return list
