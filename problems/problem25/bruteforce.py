import time
from math import log10, floor

def fib_num():
    curr = 1
    prev = 0
    f = 1

    while floor(log10(curr)) + 1 < 1000:
        next = curr + prev
        prev = curr
        curr = next
        f += 1

    return f

def main():
    start = time.time()
    ans = fib_num()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
