import time
import common
from itertools import permutations


def pandigital():
    pandigital_set = set()
    matrix = [[(i, j) for j in range(8)] for i in range(8)]

    for row in matrix:
        for pair in row:
            i, j = pair
            if i >= j:
                continue
            for p in permutations(range(1, 10)):
                if common.get_digit_value(p[0:i+1]) * \
                        common.get_digit_value(p[i+1:j+1]) == \
                        common.get_digit_value(p[j+1:]):
                    pandigital_set.add(common.get_digit_value(p[j+1:]))

    return sum(pandigital_set)


def main():
    start = time.time()
    ans = pandigital()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
