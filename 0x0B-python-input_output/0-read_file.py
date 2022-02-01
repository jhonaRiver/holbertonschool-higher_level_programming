#!/usr/bin/python3
"""
Module read_file
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_dat, end="")
