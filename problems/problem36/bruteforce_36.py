import time
import common


def palindrome(s):
    s_reversed = str()
    for c in reversed(s):
        s_reversed += c
    return s_reversed == s


def double_base():
    db_sum = 0
    for n in xrange(1000000):
        if palindrome(str(n)) and palindrome(bin(n)[2:]):
            db_sum += n
    return db_sum


def main():
    start = time.time()
    ans = double_base()
    spent = time.time() - start

    print('{0} found in {1} seconds'.format(ans, spent))


if __name__ == '__main__':
    main()
