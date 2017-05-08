import time
import common
import math


def find_num_digits_fib(n):
    phi = (math.sqrt(5) + 1) / 2
    return math.ceil(n * math.log10(phi) - (math.log10(5) / 2))


def main():
    start = time.time()
    ans = find_num_digits_fib(10*1000)
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
