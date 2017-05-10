import time
import common
from math import floor


def calc_cycle(d):
    n = r = 1
    rl = list()
    while r != 0:
        n *= 10
        r = n - (d * floor(n / d))
        if r in rl:
            break
        rl.append(r)
    return len(rl) - rl.index(r)


def cycles():
    best_cycle = 0
    best_num = 0
    for x in xrange(1000, 1, -1):
        if x < best_cycle:
            break
        c = calc_cycle(x)
        if c > best_cycle:
            best_cycle = c
            best_num = x
    return best_num


def main():
    start = time.time()
    ans = cycles()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
