# PROBLEM STATEMENT
# https://leetcode.com/problems/subtree-of-another-tree/
# Given the roots of two binary trees root and subRoot,
# return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
# The tree tree could also be considered as a subtree of itself.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.isSubtreeRecursive(root, subRoot)

    # Time Complexity: O(n) where n is the size of root
    # Space Complexity: O(1)
    def isSubtreeRecursive(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
            if not tree1 and not tree2:
                return True
            elif tree1 and tree2 and tree1.val == tree2.val:
                return isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)
            else:
                return False

        if not root and not subRoot:
            return True
        elif root and not subRoot:
            return True
        elif not root and subRoot:
            return False
        else:
            return isSameTree(root, subRoot) or self.isSubtreeRecursive(root.left, subRoot) or self.isSubtreeRecursive(
                root.right, subRoot)