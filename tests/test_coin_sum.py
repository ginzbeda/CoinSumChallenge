import unittest
from coin_sum import *


class Test(unittest.TestCase):

    def test_add_coin(self):
        coins = [1, 2, 3, 4]
        coin_index = 2
        remaining = 10
        coin_count = 0
        result_coins = []
        expected = 1, 3, [3, 3, 3]
        self.assertEqual(expected, add_coin(coins, coin_index, remaining, coin_count, result_coins))

    def test_pick_end(self):
        self.assertEqual(10, pick_middle(9, 10))

    def test_pick_start(self):
        self.assertEqual(0, pick_middle(0, 1))

    def test_pick_middle_odd(self):
        start = 0
        end = 4
        self.assertEqual(2, pick_middle(start, end))

    def test_pick_middle_even(self):
        start = 0
        end = 5
        self.assertEqual(3, pick_middle(start, end))

    def test_pick_middle_right(self):
        start = 3
        end = 7
        self.assertEqual(5, pick_middle(start, end));

    def test_index_move_on_right(self):
        coins = [1, 2, 3, 4, 5]
        coin_index = 2
        remaining = 4
        self.assertEqual(3, index_move(coins, coin_index, remaining))

    def test_index_move_on_left(self):
        coins = [1, 2, 3, 4, 5]
        coin_index = 2
        remaining = 2
        self.assertEqual(1, index_move(coins, coin_index, remaining))

    def test_index_move_to_right(self):
        coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        coin_index = 4
        remaining = 9
        self.assertEqual(7, index_move(coins, coin_index, remaining))

    def test_index_move_to_left(self):
        coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        coin_index = 4
        remaining = 2
        self.assertEqual(2, index_move(coins, coin_index, remaining))

    def test_index_move_on(self):
        coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        coin_index = 4
        remaining = 5
        self.assertEqual(4, index_move(coins, coin_index, remaining))

    def test_min_remaining_index(self):
        coins = [1, 2, 3, 4, 5]
        coin_index = 2
        remaining = 10
        self.assertEqual(3, min_remaining_index(coins, coin_index, remaining))

    def test_min_remaining_index(self):
        coins = [1, 2, 3, 4, 5]
        coin_index = 1
        remaining = 10
        self.assertEqual(1, min_remaining_index(coins, coin_index, remaining))

    def test_min_remaining_index(self):
        coins = [1, 2, 3, 4, 5]
        coin_index = 4
        remaining = 10
        self.assertEqual(4, min_remaining_index(coins, coin_index, remaining))

    def test_min_remaining_index(self):
        coins = [-1, -2, -3, -4, -5]
        coin_index = 2
        remaining = 10
        self.assertEqual(1, min_remaining_index(coins, coin_index, remaining))

    def test_coin_sum1(self):
        coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        goal_sum = 22
        self.assertEqual((3, [10, 10, 2]), coin_sum(coins, goal_sum))

    def test_coin_sum2(self):
        coins = [23]
        goal_sum = 22
        self.assertEqual((0, []), coin_sum(coins, goal_sum))

    def test_coin_sum3(self):
        coins = [-1, -2, -3]
        goal_sum = 22
        self.assertEqual((0, []), coin_sum(coins, goal_sum))

    def test_coin_sum4(self):
        coins = [2, 2, 2]
        goal_sum = 10
        self.assertEqual((5, [2, 2, 2, 2, 2]), coin_sum(coins, goal_sum))

    def test_coin_sum5(self):
        coins = [1, 2]
        goal_sum = 5
        self.assertEqual((3, [2, 2, 1]), coin_sum(coins, goal_sum))

    def test_coin_sum_empty(self):
        coins = []
        goal_sum = 5
        self.assertEqual((0, []), coin_sum(coins, goal_sum))

    def test_coin_sum_neg_mid(self):
        coins = [-4, -5, -6, 1, 2, 3, 7, 8, 9, 10]
        goal_sum = 13
        self.assertEqual((2, [10, 3]), coin_sum(coins, goal_sum))


if __name__ == '__main__':
    unittest.main()
    logging.basicConfig(level=logging.DEBUG)
