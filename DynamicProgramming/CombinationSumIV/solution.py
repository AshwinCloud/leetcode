# PROBLEM STATEMENT
# https://leetcode.com/problems/combination-sum-iv/
# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
# The test cases are generated so that the answer can fit in a 32-bit integer.
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.combinationSum4DP(nums, target)

    # Time Complexity: O(n*m) where is n is the length of nums and m is the target
    # Space Complexity: O(m) where m is the target
    def combinationSum4DP(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            # for n in nums:
            #     if i - n >= 0:
            #         dp[i] += dp[i - n]
            dp[i] = sum(map(lambda n: dp[i - n], filter(lambda n: i - n >= 0, nums)))

        return dp[target]