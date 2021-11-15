# PROBLEM STATEMENT
# https://leetcode.com/problems/same-tree/
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.isSameTreeRecursive(p, q)

    def isSameTreeRecursive(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            elif p and not q:
                return False
            elif not p and q:
                return False
            else:
                isCurrentNodeSame = p.val == q.val

                if not isCurrentNodeSame:
                    return False

                isLeftTreeSame = helper(p.left, q.left)

                if not isLeftTreeSame:
                    return False

                isRightTreeSame = helper(p.right, q.right)

                if not isRightTreeSame:
                    return False

                return True

        return helper(p, q)