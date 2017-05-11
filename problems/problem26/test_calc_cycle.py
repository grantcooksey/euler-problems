import unittest
from solution import calc_cycle


class TestCC(unittest.TestCase):
    def test_cc_3(self):
        self.assertEqual(calc_cycle(3), 1)

    def test_cc_6(self):
        self.assertEqual(calc_cycle(6), 1)

    def test_cc_7(self):
        self.assertEqual(calc_cycle(7), 6)

    def test_cc_9(self):
        self.assertEqual(calc_cycle(9), 1)

    def test_cc_11(self):
        self.assertEqual(calc_cycle(11), 2)

    def test_cc_13(self):
        self.assertEqual(calc_cycle(13), 6)

    def test_cc_17(self):
        self.assertEqual(calc_cycle(17), 16)


if __name__ == '__main__':
    unittest.main()
