import time
import common
from fractions import gcd


def cancel_digits(x, y):
    x1, x2 = (x / 10, x % 10)
    y1, y2 = (y / 10, y % 10)

    if x1 == x2 or y1 == y2:
        return False

    if (x1 == y1 and x2 / float(y2) == x / float(y)) or \
            (x2 == y1 and x1 / float(y2) == x / float(y)) or \
            (x1 == y2 and x2 / float(y1) == x / float(y)) or \
            (x2 == y2 and x1 / float(y1) == x / float(y)):
        return True

    return False



def digit_cancelling_fractions():
    prod_x = prod_y = 1
    for x in xrange(11, 100):
        for y in xrange(11, 100):
            if x % 10 == 0 or y % 10 == 0 or x >= y:
                continue
            if cancel_digits(x, y):
                prod_x *= x
                prod_y *= y
    return int(prod_y / float(gcd(prod_x, prod_y)))


def main():
    start = time.time()
    ans = digit_cancelling_fractions()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
