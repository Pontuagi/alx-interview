#!/usr/bin/python3
'''
This module contains one function
The function return the Pascal's triangle
'''

def pascal_triangle(n):
    """
    A function that returns a list of integers representing the Pascals
    triangle of n
    Returns an empty list if n <= 0
    n is assumed to always be and integer
    """
    triangle = []
    for rowNo in range(n):
        row = [1] * (rowNo + 1)
        if rowNo > 1:
            for i in range(1, rowNo):
                row[i] = triangle[rowNo - 1][i - 1] + triangle[rowNo - 1][i]
        triangle.append(row)

    return triangle

