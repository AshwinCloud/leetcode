# PROBLEM STATEMENT
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Given two integer arrays preorder and inorder where preorder is the
# preorder traversal of a binary tree and inorder is the inorder traversal of the same tree,
# construct and return the binary tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildTreeRecursive1(preorder, inorder)

    # Time Complexity: O(n)
    # Space Complexity: O(n) including the space for the result
    def buildTreeRecursive1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(preorder: List[int], inorder: List[int], preStart: int, inStart: int, inEnd: int, inorder_dict) -> Optional[TreeNode]:
            if preStart > len(preorder) - 1 or inStart > inEnd:
                return None
            else:
                root = TreeNode(preorder[preStart])

                inRootIndex = inorder_dict[preorder[preStart]]

                root.left = helper(preorder, inorder, preStart + 1, inStart, inRootIndex - 1, inorder_dict)
                root.right = helper(preorder, inorder, preStart + inRootIndex - inStart + 1, inRootIndex + 1, inEnd,
                                    inorder_dict)

                return root

        inorder_dict = {}
        for i in range(len(inorder)):
            inorder_dict[inorder[i]] = i

        return helper(preorder, inorder, 0, 0, len(inorder) - 1, inorder_dict)

    # Time Complexity: O(n)
    # Space Complexity: O(n * n) and O(n * n * n) with and without including the space for the result
    def buildTreeRecursiv2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        else:
            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            root.left = self.buildTreeRecursive(preorder[1:mid + 1], inorder[:mid])
            root.right = self.buildTreeRecursive(preorder[mid + 1:], inorder[mid + 1:])
            return root