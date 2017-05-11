import time
from math import floor


def calc_cycle(denominator):
    numerator = 1.
    remainders = list()
    while numerator != 0:
        numerator *= 10
        numerator -= denominator * floor(numerator / denominator)
        if numerator in remainders:
            break
        remainders.append(numerator)
    return len(remainders) - remainders.index(numerator)


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
