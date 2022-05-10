import logging


# # Log current info
import math

# logging.basicConfig(level=# logging.DEBUG)


# def log(coins, coin_index, remaining):
    # logging.debug('%s at: %s remaining: %d', coins[coin_index], coin_index, remaining)


# pick next middle
def pick_middle(start, end):
    # logging.info("new middle: %d", start + (end - start)//2)
    # ends of list
    if end - start == 1:
        if start == 0:
            return start
        return end
    # even try for higher
    if (end - start)%2 > 0:
        return start + (end - start) // 2
    # odd
    else:
        return (start + (end - start) // 2) + 1


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
    return pick_middle(0, len(coins)-1), remaining, coin_count, result_coins


# move index to next likely coin
def index_move(coins, coin_index, remaining):
    # logging.info("index move")
    # log(coins, coin_index, remaining)
    if not is_end(coin_index, coins):
        right_remaining = remaining - coins[coin_index+1]
        left_remaining = remaining - coins[coin_index-1]
        curr_remaining = remaining - coins[coin_index]
        if right_remaining == 0:
            return coin_index + 1
        elif left_remaining == 0:
            return coin_index - 1
        elif curr_remaining == 0:
            return coin_index
        #if current
        # if curr_remaining <= remaining or left_remaining > remaining:
        #     if abs(left_remaining) <= abs(right_remaining) \
        #             and abs(left_remaining) <= abs(remaining - coins[coin_index]):
        #         return pick_middle(0, coin_index)
        #     elif abs(right_remaining) <= abs(left_remaining) \
        #             and abs(right_remaining) <= abs(remaining - coins[coin_index]):
        #         return pick_middle(0, coin_index)
        elif (right_remaining <= left_remaining) \
                and (right_remaining <= remaining - coins[coin_index]):
            return pick_middle(coin_index, len(coins)-1)
        elif (left_remaining <= right_remaining) \
                and (left_remaining <= remaining - coins[coin_index]):
            return pick_middle(0, coin_index)
    else:
        return coin_index

def is_end(coin_index, coins):
    if coin_index == 0 or coin_index == len(coins)-1:
        return True
    return False


# Coins to reach sum goal
def coin_sum(coins, goal_sum):
    coin_index = 0
    remaining = goal_sum
    result_coins = []
    coin_count = 0
    # logging.info(coins)
    # start in the middle in case a lower coin is better
    coin_index = pick_middle(coin_index, len(coins))
    # log(coins, coin_index, remaining)
    # while has remaining and smallest coin is not too big
    while remaining != 0 \
            and coins[0] < remaining:
        prev = coin_index
        coin_index = index_move(coins, coin_index, remaining)
        coin = coins[coin_index]

        # if current index is best or is remaining
        if prev == coin_index or coin == remaining or is_end(coin_index, coins):
            coin_index, remaining, coin_count, result_coins = \
                add_coin(coins, coin_index, remaining, coin_count, result_coins)

    return coin_count, result_coins
