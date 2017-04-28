import numpy as np
import time


def amicable_pairs_numpy():
    array = np.arange(1, 10001, 1)

    func = lambda x: 2
    vfunc = np.vectorize(func)

    array = vfunc(array)

    return array.sum()


def main():
    start = time.time()
    answer = amicable_pairs_numpy()
    spent = time.time() - start

    print("Solution: {0} Time: {1:.7f}".format(answer, spent))


if __name__ == '__main__':
    main()
