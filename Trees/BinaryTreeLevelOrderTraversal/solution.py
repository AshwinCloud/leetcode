# PROBLEM STATEMENT
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
# Given the root of a binary tree, return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.levelOrderIterative(root)
    
    def levelOrderIterative(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        else:            
            queue = []
            queue.insert(0, (root, 0))
            levelOrderList = []
            while queue:
                node, height = queue.pop()                
                if len(levelOrderList) < height + 1:
                    levelOrderList.append([node.val])
                else:
                    levelOrderList[height].append(node.val)
                             
                if node.right:
                    queue.append((node.right, height+1))
                if node.left:
                    queue.append((node.left, height+1))
                    
            return levelOrderList