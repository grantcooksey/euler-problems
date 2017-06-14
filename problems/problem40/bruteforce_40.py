import time
import common


def champernowne():
    c = 1
    t = 0
    s = ''.join([str(x) for x in range(1, 1000000)])
    while t < 7:
        c *= int(s[10**t - 1])
        t += 1
    return c


def main():
    start = time.time()
    ans = champernowne()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
