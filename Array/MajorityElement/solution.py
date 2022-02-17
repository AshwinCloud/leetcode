# PROBLEM STATEMENT
# https://leetcode.com/problems/majority-element/
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.majorityElementBoyerMooreVoting(nums)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def majorityElementBoyerMooreVoting(self, nums: List[int]) -> int:
        majority = None
        count = 0

        for num in nums:
            if count == 0:
                majority = num

            if majority != num:
                count -= 1
            else:
                count += 1

        return majority