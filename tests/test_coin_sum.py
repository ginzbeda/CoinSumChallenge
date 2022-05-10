import unittest
from coin_sum import *


class Test(unittest.TestCase):

    def test_add_coin(self):
        coins = [1, 2, 3, 4]
        coin_index = 2
        remaining = 10
        coin_count = 0
        result_coins = []
        expected = 8, 1, [3]
        self.assertEqual(add_coin(coins, coin_index, remaining, coin_count, result_coins), expected)


if __name__ == '__main__':
    unittest.main()
