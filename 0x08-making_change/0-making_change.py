#!/usr/bin/python3
"""
Interview Question on: fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    :param coins: List of coin values
    :param total: Total amount to be made with coins
    :return: Fewest number of coins needed or -1 if total cannot be met
    """
    # Edge case: If total is 0 or less, return 0
    if total <= 0:
        return 0

    # sort the coins in descending order
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change
