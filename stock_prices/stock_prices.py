#!/usr/bin/python

import argparse

def find_max_profit(prices):
    profits = []
    for i in range(len(prices)-1):
        current_index = i
        for j in range(len(prices)):
            max_price = i
            if prices[j] > prices[current_index]:
                max_price = j
            profit = prices[max_price] - prices[current_index]
            if profit != 0:
                profits.append(profit)
    return max(profits)
                

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))