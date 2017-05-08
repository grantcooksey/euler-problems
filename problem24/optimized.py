import time
from math import factorial


def lexigraphic_permutation(n):
    total = factorial(10)
    available = [x for x in range(10)]

    permutation = 0

    while len(available) > 0:
        bin_size = total / len(available)

        c = 0
        current_bin = 0
        while current_bin + bin_size < n:
            current_bin += bin_size
            c += 1

        permutation *= 10
        permutation += available.pop(c)

        n = n - current_bin
        total = bin_size

    return permutation


def main():
    start = time.time()
    ans = lexigraphic_permutation(1000000)
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()