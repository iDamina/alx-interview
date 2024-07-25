#!/usr/bin/python3
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

    # Initialize the dp array with a large number (infinity)
    # dp[i] will be the minimum number of coins needed to make amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Update the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the result
    return dp[total] if dp[total] != float('inf') else -1
