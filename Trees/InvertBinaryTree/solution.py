# PROBLEM STATEMENT
# https://leetcode.com/problems/invert-binary-tree/
# Given the root of a binary tree, invert the tree, and return its root.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invertTreeRecursive(root)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def invertTreeRecursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root or (not root.left and not root.right):
                return root
            else:
                root.left = helper(root.left)
                root.right = helper(root.right)
                root.left, root.right = root.right, root.left
                return root

        return helper(root)