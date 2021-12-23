# PROBLEM STATEMENT
# https://leetcode.com/problems/coin-change/
# You are given an integer array coins representing coins of different denominations
# and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChangeDP(coins, amount)

    # Time Complexity: O(n * m) where n is the number of coins and m is the amount
    # Space Complexity: O(m) where m is the amount
    def coinChangeDP(self, coins: List[int], amount: int) -> int:
        import math
        dp = [math.inf] * (amount + 1)
        dp[0] = 0

        for a in range(amount + 1):
            for coin in coins:
                if a >= coin:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return -1 if dp[amount] == math.inf else dp[amount]

    # Time Complexity: O(n * m) + nlogn where n is the number of coins and m is the amount
    # Space Complexity: O(m) where m is the amount
    def coinChangeDPWithSort(self, coins: List[int], amount: int) -> int:
        import math
        dp = [math.inf] * (amount + 1)
        dp[0] = 0

        coins.sort()
        for a in range(amount + 1):
            for coin in coins:
                if a >= coin:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
                else:
                    break

        return -1 if dp[amount] == math.inf else dp[amount]