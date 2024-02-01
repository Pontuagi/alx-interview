#!/usr/bin/python3


"""
makeChange module
"""


def makeChange(coins, total):
    """
    A function to determine the fewest number of coins needed to meet
    a given amount total

    Args:
     - coins: The pile of coins of different value
     - total: The amount of coins to collect

    Returns:
     - 0: if total is 0 or less
     - -1: if total cannot be met by any number of coins
     - fewest number of coins to meet total
    """
    dp = [float('inf')] * (total + 1)

    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
