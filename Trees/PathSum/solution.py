# PROBLEM STATEMENT
# https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.hasPathSumRecursive(root, targetSum)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def hasPathSumRecursive(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root: Optional[TreeNode], targetSum: int) -> bool:
            if not root:
                return False
            elif not root.left and not root.right:
                return targetSum - root.val == 0
            else:
                return helper(root.left, targetSum - root.val) or helper(root.right, targetSum - root.val)

        return helper(root, targetSum)