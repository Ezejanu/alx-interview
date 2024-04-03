#!/usr/bin/python3

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

    def greedy_algorithm(coins, total):
        """
        Finds an initial solution using the greedy algorithm.

        Args:
        coins (list of int): List of available coin denominations.
        total (int): Total amount to make change for.

        Returns:
        int: Number of coins used for the initial solution.
        """

        num_coins = 0
        remaining_total = total

        for coin in coins:
            if coin <= remaining_total:
                num_coins += remaining_total // coin
                remaining_total %= coin

        return num_coins if remaining_total == 0 else float('inf')

    '''def dynamic_programming(coins, total):'''
