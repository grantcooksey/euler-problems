import time
import common
from itertools import product


def palindrome(s):
    s_reversed = str()
    for c in reversed(s):
        s_reversed += c
    return s_reversed == s


def double_base():
    db_sum = 0
    for p_tuple in product(range(10), 3):  # TODO get correct syntax for permutation with repetition
        p_num = common.get_digit_value(p_tuple)
        i = common.get_num_digits(p_num)
        p_full = (p_num * 10**i) + p_num  # Create the palindrome
        if palindrome(bin(p_full)):
            db_sum += p_full
        if i < 3:  # Odd number digits palindromes
            for middle in range(10):
                p_full = (p_num * 10**(i + 1)) + (middle * 10**i) + p_num
                if palindrome(bin(p_num)):
                    db_sum += p_full
    return db_sum


def main():
    start = time.time()
    ans = double_base()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
