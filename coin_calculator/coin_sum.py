import logging


def coin_sum(self, coins, goal_sum):
    self.coins = coins
    self.remaining = goal_sum
    self.coin_index = 0
    self.coin_count = 0
    self.result_coins = []

    def log():
        logging.debug(self.coins[self.coin_index] + " at: " + self.coin_index + " remaining : " + self.remaining)

    def pick_middle(start, end):
        logging.info("new middle: ")
        log()
        self.coin_index = (end - start)/2

    def add_coin(coin):
        logging.info("coin added: ")
        log()
        self.remaining = self.remaining - coin
        self.coin_count = self.coin_count + 1
        self.result_coins.append(coin)

    def index_move():
        logging.info("index move: ")
        log()
        right = coins[self.coin_index+1]
        left = coins[self.coin_index-1]
        if self.remaining - right == 0:
            self.coin_index = self.coin_index + 1
        elif self.remaining - left == 0:
            self.coin_index = self.coin_index - 1
        elif (self.remaining - right <= self.remaining - left) \
                and (self.remaining - right <= self.remaining - coins[self.coin_index]):
            pick_middle(self.coin_index, len(coins)-1)
        elif self.remaining - right >= self.remaining - left \
                and (self.remaining - left <= self.remaining - coins[self.coin_index]):
            pick_middle(0, self.coin_index)

    def min_coins_for_sum():
        # start in the middle in case a lower coin is better
        pick_middle(self.coin_index, len(coins))
        log()
        while self.remaining != 0 and coins[0] < self.remaining:
            coin = coins[self.coin_index]
            prev = self.coin_index
            index_move()
            if prev == self.coin_index or coin == self.remaining:
                add_coin(self.coin_index)

    logging.info("coins:" + coins + "goal_sum: " + goal_sum)
    return min_coins_for_sum()
