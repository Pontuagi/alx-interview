#!/usr/bin/python3
""" Prime Game module """


def isWinner(x, nums):
    """
    Determines the winner of a series of rounds of the game.

    Args:
    - x (int): The number of rounds.
    - nums (list): An array of integers representing the upper
    limit of consecutive integers for each round.

    Returns:
    - str or None: The name of the player that won the most rounds.
    Returns "Maria" if Maria wins the most rounds, "Ben" if Ben wins
    the most rounds, and None if the winner cannot be determined.
    """

    def is_prime(num):
        """
        Checks if a number is prime.

        Args:
        - num (int): The number to check.

        Returns:
        - bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(num):
        """
        Generates a list of prime numbers up to a given number.

        Args:
        - num (int): The upper limit for generating prime numbers.

        Returns:
        - list: A list of prime numbers up to the given number.
        """
        primes = []
        for i in range(2, num + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = get_primes(n)
        prime_count = 0
        for prime in primes:
            if prime <= n:
                prime_count += 1
            else:
                break
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
