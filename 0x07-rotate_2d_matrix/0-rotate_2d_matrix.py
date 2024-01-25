#!/usr/bin/python3

"""
Rotate 2D matrix module
"""


def rotate_2d_matrix(matrix):
    """
    A function to rotate a 2D matrix by 90 degrees

    Args:
     - Matrix: The 2D matrix to rotate

    Returns:
     - 2D Matrix rotated by 90 degrees
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
