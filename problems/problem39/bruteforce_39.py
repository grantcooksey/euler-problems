import time
import common
from math import sqrt


def right_triangles():
    p = [0] * 1001
    for a in range(1, 1001):
        for b in range(1, 1001):
            c = sqrt(a**2 + b**2)
            i = a + b + int(c)
            if c.is_integer() and i <= 1000:
                p[i] += 1
    return p.index(max(p))


def main():
    start = time.time()
    ans = right_triangles()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
