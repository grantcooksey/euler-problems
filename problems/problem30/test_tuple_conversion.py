from unittest import TestCase
from bruteforce_30 import get_digit_power_sum, get_digit_value


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
