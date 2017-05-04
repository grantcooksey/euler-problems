import time


def sum_divisors(n):
    original = n
    s = 1
    p = 2
    while p * p <= n and n > 1:
        if n % p == 0:
            j = p * p
            n = n / p
            while n % p == 0:
                j = j * p
                n = n / p
            s = s * ((j - 1) / (p - 1))
        if p == 2:
            p = 3
        else:
            p = p + 2
    if n > 1:
        s = s * (n + 1)
    return s - original


def count_non_abundant():
    end = 28124
    abundant_numbers = list()
    for i in range(1, end):
        if sum_divisors(i) > i:
            abundant_numbers.append(i)

    deficient_list = [1] * end

    for i in range(1, len(abundant_numbers)):
        for j in range(1, len(abundant_numbers)):
            if j + i < end and i != j:
                deficient_list[i+j] = 0

    non_abundant_sum = 0
    for i in range(1, end):
        if deficient_list[i] == 1:
            non_abundant_sum += i

    return non_abundant_sum


def main():
    start = time.time()
    non_abundant_sum = count_non_abundant()
    spent = time.time() - start
    print(non_abundant_sum, spent)


if __name__ == '__main__':
    main()
