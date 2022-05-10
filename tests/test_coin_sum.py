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

    def test_pick_middle_odd(self):
        start = 0
        end = 4
        self.assertEquals(pick_middle(start, end), 2)

    def test_pick_middle_even(self):
        start = 0
        end = 5
        self.assertEquals(pick_middle(start, end), 3)

    def test_pick_middle_right(self):
        start = 3
        end = 7
        self.assertEquals(pick_middle(start, end), 5)

    def test_index_move_on_right(self):
        coins = [1, 2, 3, 4, 5]
        coin_index = 2
        remaining = 4
        self.assertEqual(index_move(coins, coin_index, remaining), 3)

    def test_index_move_on_left(self):
        coins = [1, 2, 3, 4, 5]
        coin_index = 2
        remaining = 2
        self.assertEqual(index_move(coins, coin_index, remaining), 1)

    def test_index_move_to_right(self):
        coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        coin_index = 4
        remaining = 9
        self.assertEqual(index_move(coins, coin_index, remaining), 7)

    def test_index_move_to_left(self):
        coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        coin_index = 4
        remaining = 2
        self.assertEqual(index_move(coins, coin_index, remaining), 2)

    def test_index_move_on(self):
        coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        coin_index = 4
        remaining = 5
        self.assertEqual(index_move(coins, coin_index, remaining), 4)


if __name__ == '__main__':
    unittest.main()
