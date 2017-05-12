import time
import common


def spiral_sum():
    level = 1
    total = 1
    corner = 1
    while corner < 1001**2:
        space = 2 * level - 1
        corner = (2 * (level + 1) - 1)**2
        for x in range(0, 4):
            total += corner - x * (space + 1)
        level += 1
    return total


def main():
    start = time.time()
    ans = spiral_sum()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
