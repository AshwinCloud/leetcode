# PROBLEM STATEMENT
# https://leetcode.com/problems/single-number/
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return self.singleNumberXOR(nums)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def singleNumberXOR(self, nums: List[int]) -> int:
        xor = 0
        for n in nums:
            xor ^= n

        return xor

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def singleNumberMap(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            if counts.get(n):
                counts[n] += 1
            else:
                counts[n] = 1

        for n, c in counts.items():
            if c == 1:
                return n

    # Time Complexity: O(n*n)
    # Space Complexity: O(n*n)
    def singleNumberLoops(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            count = 1
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    count += 1
                    break

            if count == 1:
                return nums[i]