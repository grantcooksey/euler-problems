import time
import common


def digit_power_sum(n, power):
    power_sum = 0
    while n >= 10:
        power_sum += (n % 10)**power
        n /= 10
    power_sum += n**power
    return power_sum


def digit_fifth_powers():
    fifth_power_sum = 0

    i = 1
    while i * 9**5 > 10**i:  # find the upper bound
        i += 1

    for n in xrange(2, (i * 9**5) + 1):
        power_sum = digit_power_sum(n, 5)
        if power_sum == n:
            fifth_power_sum += power_sum

    return fifth_power_sum


def main():
    start = time.time()
    ans = digit_fifth_powers()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
