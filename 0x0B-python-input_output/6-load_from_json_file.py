#!/usr/bin/python3
"""
Module load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a JSON file
    """
    with open(filename) as f:
        return (json.load(f))
