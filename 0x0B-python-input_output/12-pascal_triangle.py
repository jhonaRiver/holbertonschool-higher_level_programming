#!/usr/bin/python3
"""
Module pascal_triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascals triangle
    of n
    """
    if n <= 0:
        return []
    t = [[1]]
    while len(t) != n:
        tri = t[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        t.append(tmp)
    return triangles
