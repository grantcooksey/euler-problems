import time
import common


def quad_primes():
    primes = set(filter(common.is_prime, range(1, 1000)))
    best = product = 0
    for a in xrange(-999, 1000, 1):
        for b in xrange(-1000, 1001, 1):
            if a % 2 == 0 and b % 2 == 0:
                continue
            n = 0
            while True:
                current_ans = n**2 + a * n + b
                if current_ans not in primes:
                    break
                n += 1
            if n > best:
                best = n
                product = a * b

    return product


def main():
    start = time.time()
    ans = quad_primes()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
