# PROBLEM STATEMENT
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.minDepthRecursive(root)

    def minDepthRecursive(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode]) -> int:
            if root.left and root.right:
                return min(helper(root.left), helper(root.right)) + 1
            elif root.left:
                return helper(root.left) + 1
            elif root.right:
                return helper(root.right) + 1
            else:
                return 1

        if not root:
            return 0
        else:
            return helper(root)