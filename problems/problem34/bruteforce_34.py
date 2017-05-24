import time
import common


def is_factorial_sum(x, fac):
    split = common.split_into_digits(x)

    factorial_sum = 0
    for d in split:
        factorial_sum += fac[d]

    return factorial_sum == x


def digit_factorials():
    fac = [1]
    for i in xrange(1, 10):
        fac += [fac[-1] * i]

    i = 1
    while i * fac[-1] > 10**i:  # find the upper bound
        i += 1

    digit_factorial_sum = 0
    for x in xrange(10, (fac[-1] * i) + 1):
        if is_factorial_sum(x, fac):
            digit_factorial_sum += x

    return digit_factorial_sum


def main():
    start = time.time()
    ans = digit_factorials()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
