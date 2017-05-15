import time
import common


def main():
    start = time.time()
    ans = len(set([a**b for b in xrange(2, 101) for a in xrange(2, 101)]))
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
