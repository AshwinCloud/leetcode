# PROBLEM STATEMENT
# https://leetcode.com/problems/longest-consecutive-sequence/
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return self.longestConsecutiveDictionary(nums)

    # Time Complexity: O(n) where n is the size of nums
    # Space Complexity: O(n)
    def longestConsecutiveDictionary(self, nums: List[int]) -> int:
        numPresentDict = {n: True for n in nums}
        global_max = 0
        for n in nums:
            if not numPresentDict.get(n - 1, False):
                local_max = 1
                i = n + 1
                while numPresentDict.get(i, False):
                    i += 1
                    local_max += 1
                global_max = max(local_max, global_max)

        return global_max