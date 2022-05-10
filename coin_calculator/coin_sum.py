import logging


# Log current info
import math


def log(coins, coin_index, remaining):
    logging.debug(coins[coin_index], " at: ", coin_index, " remaining : ", remaining)


# pick next middle
def pick_middle(start, end):
    logging.info("new middle: ", start + (end - start)//2)
    if (end - start)%2 > 0:
        return (start + (end - start) // 2) + 1
    else:
        return start + (end - start) // 2


# once coin is picked as next it is added to used coins, coin count and remaining updated
def add_coin(coins, coin_index, remaining, coin_count, result_coins):
    logging.info("coin added")
    log(coins, coin_index, remaining)
    result_coins.append(coins[coin_index])
    return remaining - coin_index, coin_count + 1, result_coins


# move index to next likely coin
def index_move(coins, coin_index, remaining):
    logging.info("index move")
    log(coins, coin_index, remaining)
    right = coins[coin_index+1]
    left = coins[coin_index-1]
    right_remaining = remaining - right
    left_remaining = remaining - left
    curr_remaining = remaining  - coins[coin_index]
    if right_remaining == 0:
        return coin_index + 1
    elif remaining - left == 0:
        return coin_index - 1
    elif curr_remaining < 0:
        if abs(left_remaining) <= abs(right_remaining) and abs(left_remaining) <= remaining - coins[coin_index]:
            return pick_middle(0, coin_index)
        elif abs(right_remaining) <= abs(left_remaining) and abs(right_remaining) <= remaining - coins[coin_index]:
            return pick_middle(0, coin_index)
    elif (0 <= abs(right_remaining) <= abs(left_remaining)) \
            and (abs(right_remaining <= remaining) - coins[coin_index]):
        return pick_middle(coin_index, len(coins)-1)
    elif (0 <= left_remaining <= right_remaining) \
            and (abs(remaining - left) <= remaining - coins[coin_index]):
        return pick_middle(0, coin_index)
    else:
        return coin_index


# Coins to reach sum goal
def coin_sum(all_coins, goal_sum):
    coin_index = 0
    coins = all_coins
    remaining = goal_sum
    result_coins = []
    coin_count = 0

    # start in the middle in case a lower coin is better
    coin_index = pick_middle(coin_index, len(coins))
    log(coins, coin_index, remaining)
    # while has remaining and smallest coin is not too big
    while remaining != 0 and coins[0] < remaining:
        prev = coin_index
        coin_index = index_move(coins, coin_index, remaining)
        coin = coins[coin_index]

        # if current index is best or is remaining
        if prev == coin_index or coin == remaining:
            remaining, coin_count, result_coins = add_coin(coins, coin_index, remaining, coin_count, result_coins)


