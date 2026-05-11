#!/usr/bin/python3
"""Module that returns a list of lists of integers
representing Pascal's triangle"""


def pascal_triangle(n):
    """Returns Pascal's triangle of n rows as a list of lists"""
    if n <= 0:
        return []

    triangle = []
    triangle.append([1])

    for i in range(n - 1):
        row = triangle[- 1]
        new = [1]

        for j in range(len(row) - 1):
            new.append(row[j] + row[j+1])

        new.append(1)
        triangle.append(new)

    return triangle
