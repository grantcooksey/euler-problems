import time


def sum_divisors(n):
    original = n
    s = 1
    p = 2
    while p * p <= n and n > 1:
        if n % p == 0:
            j = p * p
            n = n / p
            while n % p == 0:
                j = j * p
                n = n / p
            s = s * ((j - 1) / (p - 1))
        if p == 2:
            p = 3
        else:
            p = p + 2
    if n > 1:
        s = s * (n + 1)
    return s - original


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
    count = 1
    for i in xrange(count):
        start = time.time()
        answer = amicable_pairs()
        spent = time.time() - start
        total += spent

    print("Solution: {0} Time: {1:.7f} seconds average in {2} iterations".format(
        answer, total / count, count))


if __name__ == '__main__':
    main()
