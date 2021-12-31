# PROBLEM STATEMENT
# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.twoSumMap(nums, target)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def twoSumMap(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}

        for i in range(len(nums)):
            if (target - nums[i]) in index_dict:
                return [index_dict[target - nums[i]], i]
            else:
                index_dict[nums[i]] = i

        return []