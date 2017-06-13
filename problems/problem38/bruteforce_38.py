import time
import common


def is_pandigital(x, n):
    val = str()
    val_set = set()

    # Build potential pandigital
    for i in xrange(1, n + 1):
        val += str(x * i)

    # Elimitate non unique characters in potential pandigital
    for c in val:
        val_set.add(c)

    # Check for 1-9 pandigital
    if len(val) == 9 and len(val_set) == 9 and '0' not in val_set:
        return True, val
    else:
        return False, val


def pandigital_multiples():
    x = 10**4 - 1
    r = 3
    n = 2
    end = 10**r
    pandigital_list = list()
    while r > 1:
        pan, val = is_pandigital(x, n)
        if pan:
            pandigital_list.append(val)
        x -= 1
        if x <= end:
            r -= 1
            end = 10**r
            n += 1

    pandigital_list.sort()
    return pandigital_list[-1]


def main():
    start = time.time()
    ans = pandigital_multiples()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
