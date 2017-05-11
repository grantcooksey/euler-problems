"""Helpers

Collection of common functions that can be reused in later problems.
"""
from math import log10, floor, sqrt


def get_num_digits(n):
    """Number of digits in an int

    Note:
        First used in problem 25.

    :param n: an integer
    :return: number of digits in given int
    """
    return floor(log10(n)) + 1


def sum_divisors(n):
    """Sum of all divisors.

    Notes:
        Does not include the n itself in the sum.

    Args:
        n (int): Number to get sum of divisors.

    Returns:
        int: The sum of all divisors.
    """
    original = n
    s = 1
    p = 2
    while p * p <= n and n > 1:
        if n % p == 0:
            j = p * p
            n /= p
            while n % p == 0:
                j *= p
                n /= p
            s *= (j - 1) / (p - 1)
        if p == 2:
            p = 3
        else:
            p += 2
    if n > 1:
        s *= n + 1
    return s - original


def is_prime(n):
    """Checks if a number is a prime number.

    Args:
        n (int): Number to check if prime.

    Returns:
        True is prime, else False.
    """
    if n == 1:
        return False
    if n < 4:  # 2 and 3
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n < 9:  # 5 and 7
        return True

    r = floor(sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6

    return True
