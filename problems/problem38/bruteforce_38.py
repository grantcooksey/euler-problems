import time
import common


def is_pandigital(x):
    val = str()
    val_set = set()

    # Build potential pandigital
    i = 1
    while len(val) < 9:
        val += str(x * i)
        i += 1

    # Eliminate non unique characters in potential pandigital
    for c in val:
        val_set.add(c)

    # Check for 1-9 pandigital
    if len(val) == len(val_set) and '0' not in val_set:
        return True, val
    else:
        return False, val


def pandigital_multiples():
    pandigital_list = list()
    for x in range(2, 10000):
        pan, val = is_pandigital(x)
        if pan:
            pandigital_list.append(val)

    return max(pandigital_list)


def main():
    start = time.time()
    ans = pandigital_multiples()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
