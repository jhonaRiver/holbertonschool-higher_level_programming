#!/usr/bin/python3
"""
Module pascal_triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle
    of n
    """
    if n <= 0:
        return []
    t = []
    for fila in range(n):
        t.append([1])
        for a in range(1, fila):
            t[fila].append(t[fila - 1][a - 1] + t[fila - 1][a])
        if fila is not 0:
            t[fila].append(1)
    return t
