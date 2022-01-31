#!/usr/bin/python3
"""
inherits_from module
"""


def inherits_from(obj, a_class):
    """
    True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    False otheriwise
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
