#!/usr/bin/python3
"""
print_sorted module
"""


class MyList(list):
    """
    MyList class
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
