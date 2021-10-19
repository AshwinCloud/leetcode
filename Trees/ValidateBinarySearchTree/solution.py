# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTInOrderTraversal(root)
    
    def isValidBSTInOrderTraversal(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode], queue: List[TreeNode]) -> bool:
            if not root:
                return True
            else:
                isLeftBST = helper(root.left, queue)
                if not isLeftBST:
                    return False

                if queue and root.val <= queue.pop().val:
                    return False
                
                queue.append(root)
                
                isRightBST = helper(root.right, queue)
                if not isRightBST:
                    return False

                return True
        
        return helper(root, [])