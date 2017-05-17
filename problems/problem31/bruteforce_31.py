import time
import common


def coin_sums():
    # coins = [1, 2]
    coins = [1, 2, 5, 10, 20, 50 , 100]
    # goal = 5
    goal = 200
    combinations = 1

    # Populate stack with initial values
    stack = list()
    for c in coins:
        stack.append((c, coins.index(c)))

    while len(stack) != 0:
        val, max_index = stack.pop()
        if val < goal:
            index = 0
            while index <= max_index:
                stack.append((val + coins[index], index))
                index += 1
        elif val == goal:
            combinations += 1

    return combinations


def main():
    start = time.time()
    ans = coin_sums()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
