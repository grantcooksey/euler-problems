import time
from math import floor, sqrt


def sum_divisors(n):
    top = floor(sqrt(n))

    # N is a perfect square
    if n % top == 0:
        s = 1 + top
    else:
        s = 1

    if n % 2 == 1:
        start = 3
        step = 2
    else:
        start = 2
        step = 1

    while start <= top:
        if n % start == 0:
            s += start + (n / start)
        start += step

    return s


def amicable_pairs():
    s = 0
    for i in xrange(10000):
        i += 1
        div_sum = sum_divisors(i)
        if div_sum > i:
            if sum_divisors(div_sum) == i:
                s += i + div_sum
    return s


def main():
    total = 0
    count = 100
    for i in xrange(count):
        start = time.time()
        answer = amicable_pairs()
        spent = time.time() - start
        total += spent

    print("Solution: {0} Time: {1:.7f} seconds average in {2} iterations".format(
        answer, total / count, count))


if __name__ == '__main__':
    main()
