import numpy as np
import time


def sum_divisors(n):
    s = 0
    for i in range(1, n):
        if n % i == 0: s += i
    return s


def amicable_pairs_numpy():
    a = np.arange(1, 10001, 1)

    vds_func = np.vectorize(lambda x: sum_divisors(x))
    a = vds_func(a)

    return 1


def main():
    start = time.time()
    answer = amicable_pairs_numpy()
    spent = time.time() - start

    print("Solution: {0} Time: {1:.7f} seconds".format(answer, spent))


if __name__ == '__main__':
    main()
