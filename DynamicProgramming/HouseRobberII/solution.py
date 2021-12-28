# PROBLEM STATEMENT
# https://leetcode.com/problems/house-robber-ii/
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have a security system connected,
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of
# money you can rob tonight without alerting the police.
class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.robDP(nums)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def robDP(self, nums: List[int]) -> int:
        def rob(nums: List[int]) -> int:
            if len(nums) == 0:
                return 0
            elif len(nums) == 1:
                return nums[0]
            else:
                dp_prev_prev, dp_prev = nums[0], max(nums[0], nums[1])

                for i in range(2, len(nums)):
                    dp_prev_prev, dp_prev = dp_prev, max(dp_prev, dp_prev_prev + nums[i])

                return dp_prev

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(rob(nums[:-1]), rob(nums[1:]))