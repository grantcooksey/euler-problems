import unittest
from solution import calc_cycle


class MyTestCase(unittest.TestCase):
    def test_calc_cycle(self):
        self.assertEqual(calc_cycle(3), 1)
        self.assertEqual(calc_cycle(6), 1)
        self.assertEqual(calc_cycle(7), 6)
        self.assertEqual(calc_cycle(9), 1)
        self.assertEqual(calc_cycle(11), 2)
        self.assertEqual(calc_cycle(13), 6)
        self.assertEqual(calc_cycle(17), 16)


if __name__ == '__main__':
    unittest.main()
