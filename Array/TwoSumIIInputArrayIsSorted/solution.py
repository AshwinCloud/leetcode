# PROBLEM STATEMENT
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.twoSumMap(numbers, target)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def twoSumTwoPointers(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left + 1, right + 1]

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def twoSumMap(self, numbers: List[int], target: int) -> List[int]:
        compliment_dict = {}

        for i in range(len(numbers)):
            compliment = target - numbers[i]
            if compliment_dict.get(compliment) is not None:
                return [compliment_dict[compliment] + 1, i + 1]
            else:
                compliment_dict[numbers[i]] = i