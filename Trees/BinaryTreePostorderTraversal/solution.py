# PROBLEM STATEMENT
# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Given the root of a binary tree, return the postorder traversal of its nodes' values.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorderTraversalRecursive(root)

    # Time Complexity: O(n)
    # Space Complexity: O(n) including the space for the result
    def postorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root: Optional[TreeNode], l: List[int] = []) -> List[int]:
            if not root:
                return l
            else:
                helper(root.left, l)
                helper(root.right, l)
                l.append(root.val)

                return l

        return helper(root)
