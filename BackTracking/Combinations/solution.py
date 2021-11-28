# PROBLEM STATEMENT
# https://leetcode.com/problems/combinations/
# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
# You may return the answer in any order.
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.combineBacktrack(n, k)

    # Time Complexity: O(nCk)
    # Space Complexity: O(1)
    def combineBacktrack(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start: int, combination: List[int], result: List[List[int]]):
            if len(combination) == k:
                result.append(combination)
            else:
                for i in range(start, n + 1):
                    backtrack(i + 1, combination + [i], result)

        result = []
        backtrack(1, [], result)
        return result