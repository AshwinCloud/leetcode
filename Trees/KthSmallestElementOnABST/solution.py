# PROBLEM STATEMENT
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Given the root of a binary search tree, and an integer k,
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.kthSmallestIterative(root, k)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def kthSmallestIterative(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        done = 0

        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()

                done += 1
                if done == k:
                    return current.val

                current = current.right

        return 0
    