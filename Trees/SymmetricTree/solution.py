# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricRecursive(root)
        # return self.isSymmetricIterative(root)
    
    def isSymmetricRecursive(self, root: Optional[TreeNode]) -> bool:
        def helper(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            else:
                return root1.val == root2.val and helper(root1.left, root2.right) and helper(root1.right, root2.left)

        if not root:
            return True
        else:
            return helper(root.left, root.right)
    
    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            stack1 = []
            stack2 = []
            
            stack1.append(root.left)
            stack2.append(root.right)
            
            while stack1 and stack2:
                root1 = stack1.pop()
                root2 = stack2.pop()

                if not root1 and not root2:
                    continue
                if not root1 or not root2 or root1.val != root2.val:
                    return False
                else:
                    stack1.append(root1.left)
                    stack1.append(root1.right)
                    stack2.append(root2.right)
                    stack2.append(root2.left)
            
            return True