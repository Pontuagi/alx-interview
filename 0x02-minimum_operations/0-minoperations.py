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
    if n == 1:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    return dp[n] if dp[n] != float('inf') else 0
