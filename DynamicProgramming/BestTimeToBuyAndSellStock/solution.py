# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfitSinglePass(prices)
    
    def maxProfitBruteForce(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                max_profit = max(maximum, prices[j]-prices[i])
        return max_profit
    
    def maxProfitSinglePass(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_buy)
            min_buy = min(min_buy, prices[i])
        
        return max_profit