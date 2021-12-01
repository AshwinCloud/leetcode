# PROBLEM STATEMENT
# https://leetcode.com/problems/permutations/
# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permuteDFS(nums)

    # Time Complexity: O(n!)
    # Space Complexity: O(n!) for result, O(1) for additional space
    def permuteDFS(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums: List[int]):
            if len(nums) == 1:
                return [nums[:]]
            else:
                result = []

                for i in range(len(nums)):
                    removed = nums.pop()
                    perms = backtrack(nums)

                    for perm in perms:
                        perm.append(removed)

                    result.extend(perms)

                    nums.insert(0, removed)

                return result

        return backtrack(nums)