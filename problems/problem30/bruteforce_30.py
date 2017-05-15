import time
import common
from itertools import product


def get_digit_power_sum(t, power):
    return reduce(lambda rst, d: rst + d**power, t, 0)


def get_digit_value(t):
    return reduce(lambda rst, d: rst * 10 + d, t)


def digit_fifth_powers():
    fifth_power_sum = 0

    i = 1
    while i * 9**5 > 10**i:  # find the upper bound
        i += 1

    for p in product(range(10), repeat=i):
        power_sum = get_digit_power_sum(p, 5)
        digit_value = get_digit_value(p)
        if power_sum == digit_value:
            fifth_power_sum += power_sum

    return fifth_power_sum - 1  # Ignore 1 = 1^5


def main():
    start = time.time()
    ans = digit_fifth_powers()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
