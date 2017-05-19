import time
import common
from itertools import permutations


def check_pan(p, i):
    x, y, z = map(int, (p[0:i], p[i:5], p[5:]))
    return x * y == z


def pandigital():
    pandigital_set = set()
    perm_gen = (''.join(p) for p in permutations(''.join(str(c) for c in range(1, 10))))
    for p in perm_gen:
        if check_pan(p, 2) or check_pan(p, 1):
            pandigital_set.add(int(p[5:]))

    return sum(pandigital_set)


def main():
    start = time.time()
    ans = pandigital()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
