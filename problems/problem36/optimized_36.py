import time
import common
from itertools import product


def palindrome(s):
    s = s[2:]  # Remove 'b0'
    s_reversed = str()
    for c in reversed(s):
        s_reversed += c
    return s_reversed == s


def double_base():
    db_sum = 0
    for p_tuple in product(range(10), repeat=3):
        p_num = common.get_digit_value(p_tuple)
        p_reversed = int(str(p_num)[::-1])

        if p_num == 0:
            continue

        i = common.get_num_digits(p_num)
        p_full = (p_num * 10**i) + p_reversed  # Create the palindrome
        if palindrome(bin(p_full)):
            db_sum += p_full
        if i < 3:  # Odd number digits palindromes
            for middle in range(10):
                p_full = (p_num * 10**(i + 1)) + (middle * 10**i) + p_reversed
                if palindrome(bin(p_full)):
                    db_sum += p_full

    # Check for single digit palindromes
    for n in xrange(1, 10):
        if palindrome(bin(n)):
            db_sum += n

    return db_sum


def main():
    start = time.time()
    ans = double_base()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
