# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthRecursion(root)
    
    def maxDepthRecursion(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            else:
                return max(helper(root.left), helper(root.right)) + 1
            
        return helper(root)