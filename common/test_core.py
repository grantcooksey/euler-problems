from unittest import TestCase
from core import is_prime, get_digit_power_sum, get_digit_value, \
    split_into_digits, prime_sieve


class TestPrimeSieve(TestCase):
    def test_sieve_10(self):
        self.assertEquals(prime_sieve(10), [2, 3, 5, 7])

    def test_sieve_0(self):
        self.assertEquals(prime_sieve(0), list())

    def test_sieve_25(self):
        self.assertEquals(prime_sieve(25), [2, 3, 5, 7, 11, 13, 17, 19, 23])


class TestIsPrime(TestCase):
    def test_is_prime_2(self):
        self.assertEquals(is_prime(2), True)

    def test_is_prime_3(self):
        self.assertEquals(is_prime(3), True)

    def test_is_prime_13(self):
        self.assertEquals(is_prime(13), True)

    def test_is_prime_907(self):
        self.assertEquals(is_prime(907), True)

    def test_is_prime_401(self):
        self.assertEquals(is_prime(401), True)

    def test_is_prime_1(self):
        self.assertEquals(is_prime(1), False)

    def test_is_prime_9(self):
        self.assertEquals(is_prime(9), False)

    def test_is_prime_15(self):
        self.assertEquals(is_prime(15), False)

    def test_is_prime_1219(self):
        self.assertEquals(is_prime(1219), False)


class TestTupleConversion(TestCase):
    def test_get_digit_power_sum_1634(self):
        self.assertEqual(get_digit_power_sum((1, 6, 3, 4), 4), 1634)

    def test_get_digit_power_sum_20(self):
        self.assertEqual(get_digit_power_sum((2, 0), 5), 32)

    def test_get_digit_power_sum_9474(self):
        self.assertEqual(get_digit_power_sum((9, 4, 7, 4), 4), 9474)

    def test_get_digit_value_1637(self):
        self.assertEqual(get_digit_value((1, 6, 3, 7)), 1637)

    def test_get_digit_value_20(self):
        self.assertEqual(get_digit_value((2, 0)), 20)

    def test_get_digit_value_9474(self):
        self.assertEqual(get_digit_value((9, 4, 7, 4)), 9474)


class TestSplitNumber(TestCase):
    def test_split_digits_1637(self):
        self.assertEqual(split_into_digits(1637), [1, 6, 3, 7])

    def test_split_digits_1(self):
        self.assertEqual(split_into_digits(1), [1])

    def test_split_digits_20(self):
        self.assertEqual(split_into_digits(20), [2, 0])