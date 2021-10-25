# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return self.containsDuplicateSort(nums)
        
    def containsDuplicateDictionary(self, nums: List[int]) -> bool:
        dictionary = {}
        
        for n in nums:
            if dictionary.get(n):
                return True
            else:
                dictionary[n] = True
        
        return False
    
    def containsDuplicateSort(self, nums: List[int]) -> bool:
        nums.sort()
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        
        return False