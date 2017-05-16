"""Helpers

This module contains a collection of common functions that can be reused in
later problems. There is no criteria as to when it is a good idea to transfer
a function from the problem to the core module other than it might be helpful.
"""
from math import log10, floor, sqrt


def get_num_digits(n):
    """Number of digits.

    A mathematical approach to calculating the number of digits in a number.
    This method is an alternative to converting the number to a string and
    calculating the length of the string. This method works well when counting
    digits for a large number since converting an int to a string is costly.

    Args:
        n (int): Number to get the number of digits from

    Returns:
        int: Number of digits in n.
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


def get_digit_power_sum(t, power):
    """Sum of power of each digit.

    Sums each digit raised by the power.

    Args:
        t (tuple): tuple of single digit positive ints.
        power (int): power to raise each digit.

    Returns:
        int: Sum of digits raised by the power.
    """
    return reduce(lambda rst, d: rst + d**power, t, 0)


def get_digit_value(t):
    """Converts a tuple into number.

    Args:
        t (tuple): tuple of single digit positive ints.

    Returns:
        int: Number the tuple represents.

    """
    return reduce(lambda rst, d: rst * 10 + d, t)


def split_into_digits(n):
    """Splits an int into a list of ints.

    Args:
        n (int): Number to split.

    Returns:
        list: List of ints.

    """
    digits = list()
    while n >= 10:
        digits = [n % 10] + digits
        n /= 10
    digits = [n] + digits
    return digits
