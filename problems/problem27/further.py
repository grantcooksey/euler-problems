import time
import common


def gen_primes(n):
    while n > 0:
        if common.is_prime(n):
            yield n
        n -= 1


def quad_primes():
    prime_set = set([i for i in gen_primes(1999)])  # First 1999 primes
    b_set = filter(lambda x: x < 1000, prime_set)
    best = product = 0
    for a in xrange(-999, 1000, 2):  # a is odd
        for b in b_set:  # b is prime
            n = 0
            while True:
                current_ans = n**2 + a * n + b
                if current_ans not in prime_set:
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
