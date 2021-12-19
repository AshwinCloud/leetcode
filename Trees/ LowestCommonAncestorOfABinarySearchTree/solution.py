# PROBLEM STATEMENT
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T
# that has both p and q as descendants (where we allow a node to be a descendant of itself).”
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lowestCommonAncestorRecursive(root, p, q)

    # Time Complexity: O(n/2)
    # Space Complexity: O(1)
    def lowestCommonAncestorRecursive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if not root:
                return None
            elif p.val > root.val and q.val > root.val:
                return helper(root.right, p, q)
            elif p.val < root.val and q.val < root.val:
                return helper(root.left, p, q)
            else:
                return root

        return helper(root, p, q)