import logging
import math

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
    return index_move(coins, coin_index, remaining), remaining, coin_count, result_coins


# move index to next likely coin
def index_move(coins, coin_index, remaining):
    logging.debug("index move")
    log(coins, coin_index, remaining)
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


# find next index direction
def min_remaining_index(coins, coin_index, remaining):
    # all possible directions
    curr_remaining = remaining - coins[coin_index]
    # current is exact
    if coins[coin_index] == remaining:
        return coin_index
    # set present possibilities
    if coin_index + 1 <= len(coins) - 1:
        right_remaining = remaining - coins[coin_index + 1]
    else:
        right_remaining = None
    if coin_index - 1 >= 0:
        left_remaining = remaining - coins[coin_index - 1]
    else:
        left_remaining = None

    # compare available directions
    # all three possibilities present
    if left_remaining is not None and right_remaining is not None:
        logging.debug("All directions possible")
        # find best
        # account for negative
        if left_remaining < 0 and right_remaining < 0 and curr_remaining < 0:
            direction = max(left_remaining, right_remaining, curr_remaining)
        elif left_remaining < 0 and curr_remaining < 0:
            direction = right_remaining
        elif right_remaining < 0 and curr_remaining < 0:
            direction = left_remaining
        else:
            direction = min(left_remaining, right_remaining, curr_remaining)
        # check best
        if direction == left_remaining:
            return coin_index - 1
        elif direction == right_remaining:
            return coin_index + 1
        else:
            return coin_index

    # left impossible
    elif right_remaining is not None:
        logging.debug("Left direction impossible")
        # find best
        # account for negative
        if right_remaining < 0 and curr_remaining < 0:
            direction = max(right_remaining, curr_remaining)
        else:
            direction = min(right_remaining, curr_remaining)
        # check best
        if direction == right_remaining or right_remaining == 0:
            return coin_index + 1
        else:
            return coin_index

    # right impossible
    elif left_remaining is not None:
        logging.debug("Right direction impossible")
        # find best
        # account for negative
        if left_remaining < 0 and curr_remaining < 0:
            direction = max(left_remaining, curr_remaining)
        else:
            direction = min(left_remaining, curr_remaining)
        # check best
        if direction == left_remaining or left_remaining == 0:
            return coin_index - 1
        else:
            return coin_index
    # current
    else:
        logging.debug("stick to current")
        return coin_index


# check if at endpoint
def is_end(coin_index, coins):
    if coin_index == 0 or coin_index == len(coins) - 1:
        logging.debug("At endpoint: %d", coin_index)
        return True
    return False


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
    first_coin = coins[0]
    logging.info("Starting with coins: %s " % coins)
    logging.info("Goal sum: %d", goal_sum)

    # no coins available
    coin_index = pick_middle(coin_index, len(coins) - 1)
    logging.debug("New index: %d", coin_index)
    log(coins, coin_index, remaining)

    # while has remaining and smallest coin is not too big and positive
    while remaining != 0 \
            and first_coin <= remaining \
            and (remaining - first_coin < remaining or first_coin < 0):
        prev = coin_index
        coin_index = index_move(coins, coin_index, remaining)
        logging.debug("New index: %d", coin_index)
        coin = coins[coin_index]
        logging.debug("moving from %d to %d", prev, coin_index)

        # if current index is best or is remaining or endpoint was reached add coins
        if prev == coin_index or coin == remaining or (is_end(coin_index, coins)):
            # only negative coins available
            if is_end(coin_index, coins) and remaining - coins[coin_index] > remaining:
                logging.info("final return coin count: %d", coin_count)
                logging.info("final return result coins: %s" % result_coins)
                return coin_count, result_coins
            coin_index, remaining, coin_count, result_coins = \
                add_coin(coins, coin_index, remaining, coin_count, result_coins)
            logging.debug("added: %s", result_coins)
            logging.debug("with coin count: %d", coin_count)
    logging.info("final return coin count: %d", coin_count)
    logging.info("final return result coins: %s" % result_coins)
    return coin_count, result_coins
