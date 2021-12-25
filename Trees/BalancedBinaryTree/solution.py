# PROBLEM STATEMENT
# https://leetcode.com/problems/balanced-binary-tree/
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedRecursive(root)

    # Time Complexity: O(n ^ 2)
    # Space Complexity: O(1)
    def isBalancedRecursive(self, root: Optional[TreeNode]) -> bool:
        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            else:
                return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        else:
            return -1 <= height(root.left) - height(root.right) <= 1 and self.isBalancedRecursive(
                root.left) and self.isBalancedRecursive(root.right)