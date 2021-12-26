# PROBLEM STATEMENT
# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Given the root of a binary tree, return the preorder traversal of its nodes' values.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.preorderTraversalRecursive(root)

    def preorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root: Optional[TreeNode], preorder_list: List[int] = []) -> List[int]:
            if not root:
                return preorder_list
            else:
                preorder_list.append(root.val)
                helper(root.left, preorder_list)
                helper(root.right, preorder_list)

                return preorder_list

        return helper(root)