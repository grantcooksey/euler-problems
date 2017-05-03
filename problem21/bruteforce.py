import time
#from math import floor, sqrt
#
#
#def sum_divisors(n):
#    top = floor(sqrt(n))
#
#    # N is a perfect square
#    if n % top == 0:
#        s = 1 + top
#    else:
#        s = 1
#
#    if n % 2 == 1:
#        start = 3
#        step = 2
#    else:
#        start = 2
#        step = 1
#
#    while start <= top:
#        if n % start == 0:
#            s += start + (n / start)
#        start += step
#
#    return s


def sum_divisors(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s


def amicable_pairs():
    generator = ((i+215, sum_divisors(i+215)) for i in xrange(10000))
    div_dictionary = dict()
    amicable_pairs_sum = 0
    for num, div_sum in generator:
        if num > div_sum:
            if num in div_dictionary:
                if div_sum in div_dictionary[num]:  # Found an amicable pair
                    amicable_pairs_sum += num + div_sum
        else:  # Need to add div_sum to set in dictionary
            if div_sum not in div_dictionary:
                div_dictionary[div_sum] = set()
            div_dictionary[div_sum].add(num)
        div_dictionary.pop(num, None)  # Used to trim dic
    return amicable_pairs_sum


def main():
    total = 0
    count = 100
    for i in xrange(count):
        start = time.time()
        answer = amicable_pairs()
        spent = time.time() - start
        total += spent

    print("Solution: {0} Time: {1:.7f} seconds average in {2} iterations".format(
        answer, total / count, count))


if __name__ == '__main__':
    main()
