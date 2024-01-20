#!/usr/bin/python3

"""
This module contains a function that checks the number of minimum operations to
complete a task
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to achieve n H
    characters.

    Args:
    - n: Integer, the desired number of H characters

    Returns:
    - Integer, the minimum number of operations needed
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)
    return n
