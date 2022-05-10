import logging

# # Log current info
import math


# logging.basicConfig(level=# logging.DEBUG)


# def log(coins, coin_index, remaining):
# logging.debug('%s at: %s remaining: %d', coins[coin_index], coin_index, remaining)


# pick next middle
def pick_middle(start_index, end_index):
    # logging.info("new middle: %d", start + (end - start)//2)
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
    # logging.info("coin added")
    # log(coins, coin_index, remaining)
    # already found greatest coin
    # use as many times as possible
    while remaining >= coins[coin_index]:
        result_coins.append(coins[coin_index])
        coin_count = coin_count + 1
        remaining = remaining - coins[coin_index]
    return index_move(coins, coin_index, remaining), remaining, coin_count, result_coins


# move index to next likely coin
def index_move(coins, coin_index, remaining):
    # logging.info("index move")
    # log(coins, coin_index, remaining)
    direction = min_remaining_index(coins, coin_index, remaining)
    if direction == coin_index:
        return coin_index
    if coins[direction] == remaining:
        return direction
    if is_end(coin_index, coins):
        return direction
    if direction == coin_index + 1:
        return pick_middle(coin_index, len(coins) - 1)
    else:
        return pick_middle(0, coin_index)


    # curr_remaining = remaining - coins[coin_index]
    # if coin_index + 1 <= len(coins) - 1:
    #     right_remaining = coins[coin_index + 1]
    # else:
    #     right_remaining = None
    # if coin_index - 1 >= 0:
    #     left_remaining = coins[coin_index + 1]
    # else:
    #     left_remaining = None
    # if not is_end(coin_index, coins):
    #     if right_remaining == 0:
    #         return coin_index + 1
    #     elif left_remaining == 0:
    #         return coin_index - 1
    #     elif curr_remaining == 0:
    #         return coin_index
    #     if right_remaining > remaining or right_remaining < 0 \
    #             and left_remaining > remaining or left_remaining < 0 \
    #             and curr_remaining > remaining or curr_remaining < 0:
    #         if abs(left_remaining) <= abs(right_remaining) \
    #                 and abs(left_remaining) <= abs(remaining - coins[coin_index]):
    #             return pick_middle(0, coin_index)
    #         elif abs(right_remaining) <= abs(left_remaining) \
    #                 and abs(right_remaining) <= abs(remaining - coins[coin_index]):
    #             return pick_middle(0, coin_index)
    #     elif (right_remaining <= left_remaining) \
    #             and (right_remaining <= curr_remaining):
    #         return pick_middle(coin_index, len(coins) - 1)
    #     elif (left_remaining <= right_remaining) \
    #             and (left_remaining <= curr_remaining):
    #         return pick_middle(0, coin_index)
    # elif coin_index == 0 and coin_index + 1 <= len(coins) - 1 and remainingcoins[coin_index + 1]:
    #     return -1
    # else:
    #     return coin_index


def min_remaining_index(coins, coin_index, remaining):
    # all possible directions
    curr_remaining = remaining - coins[coin_index]
    if coins[coin_index] == remaining:
        return coin_index
    if coin_index + 1 <= len(coins) - 1:
        right_remaining = remaining - coins[coin_index + 1]
    else:
        right_remaining = None
    if coin_index - 1 >= 0:
        left_remaining = remaining - coins[coin_index - 1]
    else:
        left_remaining = None

    # compare available directions
    # all three
    if left_remaining is not None and right_remaining is not None:
        if left_remaining < 0 and right_remaining < 0 and curr_remaining < 0:
            direction = max(left_remaining, right_remaining, curr_remaining)
        elif left_remaining < 0 and curr_remaining < 0:
            direction = right_remaining
        elif right_remaining < 0 and curr_remaining < 0:
            direction = left_remaining
        else:
            direction = min(left_remaining, right_remaining, curr_remaining)
        if direction == left_remaining:
            return coin_index - 1
        elif direction == right_remaining:
            return coin_index + 1
        else:
            return coin_index
    # right compare
    elif right_remaining is not None:
        if right_remaining < 0 and curr_remaining < 0:
            direction = max(right_remaining, curr_remaining)
        else:
            direction = min(right_remaining, curr_remaining)
        if direction == right_remaining or right_remaining == 0:
            return coin_index + 1
        else:
            return coin_index
    # left compare
    elif left_remaining is not None:
        if left_remaining < 0 and curr_remaining < 0:
            direction = max(left_remaining, curr_remaining)
        else:
            direction = min(left_remaining, curr_remaining)
        if direction == left_remaining or left_remaining == 0:
            return coin_index - 1
        else:
            return coin_index
    # current
    else:
        return coin_index


def is_end(coin_index, coins):
    if coin_index == 0 or coin_index == len(coins) - 1:
        return True
    return False


# Coins to reach sum goal
def coin_sum(coins, goal_sum):
    coin_index = 0
    remaining = goal_sum
    result_coins = []
    coin_count = 0
    first_coin = coins[0]
    # logging.info(coins)
    # start in the middle in case a lower coin is better
    if is_end(coin_index, coins):
        coin_index = index_move(coins, coin_index, remaining)
    else:
        coin_index = pick_middle(coin_index, len(coins) - 1)
    # log(coins, coin_index, remaining)
    # while has remaining and smallest coin is not too big
    while remaining != 0 \
            and first_coin <= remaining \
            and remaining - first_coin < remaining:
        prev = coin_index
        coin_index = index_move(coins, coin_index, remaining)
        if coin_index == -1:
            return 0, []
        coin = coins[coin_index]

        # if current index is best or is remaining
        if prev == coin_index or coin == remaining or is_end(coin_index, coins):
            coin_index, remaining, coin_count, result_coins = \
                add_coin(coins, coin_index, remaining, coin_count, result_coins)

    return coin_count, result_coins
