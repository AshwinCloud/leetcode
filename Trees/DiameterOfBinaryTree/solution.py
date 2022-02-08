# PROBLEM STATEMENT
# https://leetcode.com/problems/diameter-of-binary-tree/
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.diameterOfBinaryTreeRecursive(root)

    # Time Complexity: O(n) where n is the size of the tree
    # Space Complexity: O(1)
    def diameterOfBinaryTreeRecursive(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], maxDiameter: List[int]) -> int:
            if not root:
                return -1
            else:
                left = dfs(root.left, maxDiameter)
                right = dfs(root.right, maxDiameter)
                height = 1 + max(left, right)
                diameter = 2 + left + right
                maxDiameter[0] = max(maxDiameter[0], diameter)
                return height

        maxDiameter = [0]
        dfs(root, maxDiameter)
        return maxDiameter[0]