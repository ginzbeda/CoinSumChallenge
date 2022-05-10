import logging
import math
from re import match
from unittest import case

logging.basicConfig(level=logging.INFO)


# logger for getting current info
def log(coins, coin_index, remaining):
    logging.debug('%s at: %s remaining: %d', coins[coin_index], coin_index, remaining)


# pick next middle
def pick_middle(start_index, end_index):
    logging.debug("new middle: %d", start_index + (end_index - start_index)//2)
    # ends of list
    if end_index - start_index == 1:
        if start_index == 0:
            return start_index
        return end_index
    # even try for higher
    if ((end_index - start_index) + 1) % 2 == 0:
        return start_index + ((end_index - start_index) + 1) // 2
    # odd
    else:
        return start_index + (end_index - start_index) // 2


# once coin is picked as next it is added to used coins, coin count and remaining updated
def add_coin(coins, coin_index, remaining, coin_count, result_coins):
    logging.debug("Coin added: %d", coins[coin_index])
    log(coins, coin_index, remaining)
    # already found greatest coin
    # use as many times as possible
    while remaining >= coins[coin_index]:
        result_coins.append(coins[coin_index])
        coin_count = coin_count + 1
        remaining = remaining - coins[coin_index]
    return remaining, coin_count, result_coins
#
#
# # move index to next likely coin
# def index_move(coins, coin_index, remaining):
#     logging.debug("index move")
#     log(coins, coin_index, remaining)
#     direction = min_remaining_index(coins, coin_index, remaining)
#     if direction == coin_index:
#         return coin_index
#     if coins[direction] == remaining:
#         return direction
#     if is_end(coin_index, coins):
#         return direction
#     if direction == coin_index + 1:
#         return pick_middle(coin_index, len(coins) - 1)
#     else:
#         return pick_middle(0, coin_index)
#
#
# # find next index direction
# def min_remaining_index(coins, coin_index, remaining):
#     # all possible directions
#     curr_remaining = remaining - coins[coin_index]
#     # current is exact
#     if coins[coin_index] == remaining:
#         return coin_index
#     # set present possibilities
#     if coin_index + 1 <= len(coins) - 1:
#         right_remaining = remaining - coins[coin_index + 1]
#     else:
#         right_remaining = None
#     if coin_index - 1 >= 0:
#         left_remaining = remaining - coins[coin_index - 1]
#     else:
#         left_remaining = None
#
#     # compare available directions
#     # all three possibilities present
#     if left_remaining is not None and right_remaining is not None:
#         logging.debug("All directions possible")
#         # find best
#         # account for negative
#         if left_remaining < 0 and right_remaining < 0 and curr_remaining < 0:
#             direction = max(left_remaining, right_remaining, curr_remaining)
#         elif left_remaining < 0 and curr_remaining < 0:
#             direction = right_remaining
#         elif right_remaining < 0 and curr_remaining < 0:
#             direction = left_remaining
#         else:
#             direction = min(left_remaining, right_remaining, curr_remaining)
#         # check best
#         if direction == left_remaining:
#             return coin_index - 1
#         elif direction == right_remaining:
#             return coin_index + 1
#         else:
#             return coin_index
#
#     # left impossible
#     elif right_remaining is not None:
#         logging.debug("Left direction impossible")
#         # find best
#         # account for negative
#         if right_remaining < 0 and curr_remaining < 0:
#             direction = max(right_remaining, curr_remaining)
#         else:
#             direction = min(right_remaining, curr_remaining)
#         # check best
#         if direction == right_remaining or right_remaining == 0:
#             return coin_index + 1
#         else:
#             return coin_index
#
#     # right impossible
#     elif left_remaining is not None:
#         logging.debug("Right direction impossible")
#         # find best
#         # account for negative
#         if left_remaining < 0 and curr_remaining < 0:
#             direction = max(left_remaining, curr_remaining)
#         else:
#             direction = min(left_remaining, curr_remaining)
#         # check best
#         if direction == left_remaining or left_remaining == 0:
#             return coin_index - 1
#         else:
#             return coin_index
#     # current
#     else:
#         logging.debug("stick to current")
#         return coin_index


# check if at endpoint
def is_end(coin_index, coins):
    if coin_index == 0 or coin_index == len(coins) - 1:
        logging.debug("At endpoint: %d", coin_index)
        return True
    return False


def find_next(coins, remaining, index_offset):
    first = 0
    first_remaining = remaining - coins[first]
    if not is_end(first, coins):
        mid_index = pick_middle(0, len(coins))
        last = len(coins)-1
        mid = mid_index
        mid_remaining = remaining - coins[mid]
        last_remaining = remaining - coins[last]
        min_remaining = min(first_remaining, mid_remaining, last_remaining)

        if len(coins) == 1:
            return

        if (last_remaining > remaining or last_remaining < 0) and (first_remaining > remaining or first_remaining < 0) and (mid_remaining > remaining or mid_remaining < 0):
            return -1
        if last_remaining > remaining or last_remaining < 0:
            return find_next(coins[first:last - 1], remaining, index_offset)
        if first_remaining > remaining or first_remaining < 0:
            return find_next(coins[first + 1:last], remaining, index_offset + 1)

        if min_remaining == first_remaining:
            return find_next(coins[0:mid_index], remaining, index_offset)
        elif min_remaining == last_remaining:
            return find_next(coins[mid_index:len(coins)-1], remaining, index_offset + mid_index)
        else:
            return mid_index + index_offset

    elif len(coins) > 1:
        last = len(coins)-1
        last_remaining = remaining - coins[last]
        min_remaining = min(first_remaining, last_remaining)
        if (first_remaining > remaining or first_remaining < 0) and (last_remaining > remaining or last_remaining < 0):
            return -1
        elif last_remaining > remaining or last_remaining < 0:
            return first + index_offset
        elif first_remaining > remaining or first_remaining < 0:
            return last + index_offset
    else:
        return 0 + index_offset


# Coins to reach sum goal
# returns: number of coins used, coins used
def coin_sum(coins, goal_sum):
    coin_index = 0
    remaining = goal_sum
    result_coins = []
    coin_count = 0
    # no coins possible
    if len(coins) == 0:
        logging.warning("no coins available")
        logging.info("final return coin count: %d", coin_count)
        logging.info("final return result coins: %s" % result_coins)
        return 0, []
    while remaining > 0:
        remaining, coin_count, result_coins = \
            add_coin(coins, find_next(coins, goal_sum, 0), remaining, coin_count, result_coins)

    return coin_count, result_coins


if __name__ == '__main__':
    input_coins = [int(item) for item in input("Please enter coins available (example: 1 2 3 4): ").split()]
    sum_goal = int(input("please enter sum goal: "))
    result = coin_sum(input_coins, sum_goal)