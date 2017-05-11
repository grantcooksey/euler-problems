from unittest import TestCase
from core import is_prime


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
