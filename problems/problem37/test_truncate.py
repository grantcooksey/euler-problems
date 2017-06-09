from unittest import TestCase
from common import prime_sieve
from bruteforce_37 import truncate


class TestTruncate(TestCase):
    def test_truncate_3797(self):
        self.assertTrue(truncate(3797, prime_sieve(1000000)))

    def test_truncate_3792(self):
        self.assertFalse(truncate(3792, prime_sieve(1000000)))

    def test_truncate_92(self):
        self.assertFalse(truncate(92, prime_sieve(1000000)))

    def test_truncate_311(self):
        self.assertFalse(truncate(311, prime_sieve(1000000)))

    def test_truncate_748317(self):
        self.assertFalse(truncate(748317, prime_sieve(1000000)))
