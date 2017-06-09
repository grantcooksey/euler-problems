import time
import common


def truncate(prime, prime_set):
    curr = prime
    left = list()

    # truncate right
    while curr != 0:
        if curr not in prime_set:
            return False
        left.append(curr % 10)
        curr /= 10

    # truncate left
    curr = prime
    while len(left) > 1:
        first_digit = left.pop(-1)
        curr -= first_digit * 10 ** len(left)
        if curr not in prime_set:
            return False

    return True


def first_last_digit_prime(x, primes):
    last_digit = x % 10
    first_digit = x / 10**(common.get_num_digits(x) - 1)
    return last_digit in primes and first_digit in primes


def truncatable_primes():
    primes = common.prime_sieve(1000000)
    prime_set = set(primes)

    under_10 = primes[:4]
    primes = primes[4:]  # Ignore single digits primes

    # Filter primes where first and last digit are not prime
    # primes = filter(lambda x: first_last_digit_prime(x, under_10), primes)

    truncatable_sum = 0

    for p in primes:
        if truncate(p, prime_set):
            truncatable_sum += p

    return truncatable_sum


def main():
    start = time.time()
    ans = truncatable_primes()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
