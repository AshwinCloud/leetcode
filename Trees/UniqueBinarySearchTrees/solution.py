# PROBLEM STATEMENT
# https://leetcode.com/problems/unique-binary-search-trees/
# Given an integer n, return the number of structurally unique BST's (binary search trees)
# which has exactly n nodes of unique values from 1 to n.
class Solution:
    def numTrees(self, n: int) -> int:
        return self.numTreesDP(n)

    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def numTreesDP(self, n: int) -> int:
        numTrees = [1] * (n + 1)

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += numTrees[left] * numTrees[right]
            numTrees[nodes] = total

        return numTrees[n]