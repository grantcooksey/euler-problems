"""Helpers

Collection of common functions that can be reused in later problems.
"""
from math import log10, floor


def get_num_digits(n):
    """Number of digits in an int

    Note:
        First used in problem 25.

    :param n: an integer
    :return: number of digits in given int
    """
    return floor(log10(n)) + 1


def sum_divisors(n):
    """Sum of all divisors

    Calculates the sum of all divisors of a number excluding the number itself.

    :param n: int to find the sum
    :return: int sum
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
