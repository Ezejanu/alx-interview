#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the given total amount
    using a combination of greedy algorithm and dynamic programming.

    Args:
    coins (list of int): List of available coin denominations.
    total (int): Total amount to make change for.

    Returns:
    int: Fewest number of coins needed to meet the total amount. Returns -1
    if the total cannot be met by any combination of coins.

    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order

    num_coins = 0
    remaining_total = total

    for coin in coins:
        if coin <= remaining_total:
            num_coins += remaining_total // coin
            remaining_total %= coin

    if remaining_total == 0:
        return num_coins
    else:
        return -1
