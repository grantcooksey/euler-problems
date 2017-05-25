import time
import common


def circular_primes():
    sieve = set(common.prime_sieve(1000000))
    num_circular = 0
    for prime in sieve:
        digits = common.get_num_digits(prime)
        circular = True
        for i in xrange(digits):
            first = prime / 10**(digits - 1)
            rest = prime % 10**(digits - 1)
            prime = rest * 10 + first
            if prime not in sieve:
                circular = False
                break
        if circular:
            num_circular += 1
    return num_circular


def main():
    start = time.time()
    ans = circular_primes()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
