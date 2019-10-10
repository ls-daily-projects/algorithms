#!/usr/bin/python

import argparse

# Time: O(n * n-1) => O(n^2)
# Space: O(1)


def find_max_profit(prices):
    prices_count = len(prices)

    if (prices_count < 1):
        return 0

    if (prices_count == 1):
        return prices[0]

    max_profit = prices[1] - prices[0]

    for buy_index, buy_price in enumerate(prices):
        sell_index = buy_index + 1

        while(sell_index < prices_count):
            sell_price = prices[sell_index]
            current_profit = sell_price - buy_price
            max_profit = current_profit if current_profit > max_profit else max_profit
            sell_index += 1

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
