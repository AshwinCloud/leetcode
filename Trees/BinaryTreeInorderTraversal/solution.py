# PROBLEM STATEMENT
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversalRecursive(root)

    def inorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root: Optional[TreeNode], inorder_list: List[int]):
            if root:
                helper(root.left, inorder_list)
                inorder_list.append(root.val)
                helper(root.right, inorder_list)

        inorder_list = []
        helper(root, inorder_list)
        return inorder_list
