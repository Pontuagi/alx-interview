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
        return 0  # Handle non-positive integer inputs
    operations = [0] * (n + 2)

    for i in range(2, n + 1):
        if operations[i] == 0:
            for j in range(i * 2, n + 1, i):
                if operations[j] == 0:
                    operations[j] = operations[i] + (j // i)

    return operations[n]
