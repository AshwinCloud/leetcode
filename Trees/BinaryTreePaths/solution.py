# PROBLEM STATEMENT
# https://leetcode.com/problems/binary-tree-paths/
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.binaryTreePathsList(root)

    # Time Complexity: O(n)
    # Space Complexity: O(h * l) where h is the height of the tree and l is the number of leaf trees. O(n^2) at worst
    def binaryTreePathsList(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root: Optional[TreeNode], curr_list: List[int] = [], final_list: List[str] = []) -> List[str]:
            if not root:
                return final_list
            else:
                curr_list.append(root.val)

                if root.left and root.right:
                    curr_list_copy = curr_list.copy()
                    helper(root.left, curr_list, final_list)
                    helper(root.right, curr_list_copy, final_list)
                elif root.left:
                    helper(root.left, curr_list, final_list)
                elif root.right:
                    helper(root.right, curr_list, final_list)
                else:
                    final_list.append(listToStr(curr_list))

                return final_list

        def listToStr(l: List[int]) -> str:
            if not l:
                return ""
            else:
                s = str(l[0])
                for i in range(1, len(l)):
                    s += "->" + str(l[i])
                return s

        return helper(root)

    # Time Complexity: O(n)
    # Space Complexity: O(h * l) where h is the height of the tree and l is the number of leaf trees. O(n^2) at worst
    def binaryTreePathsString(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root: Optional[TreeNode], final_list: List[str] = [], curr_str: str = "") -> List[str]:
            if not root:
                return final_list
            else:
                if not curr_str:
                    curr_str += str(root.val)
                else:
                    curr_str += "->" + str(root.val)

                if not root.left and not root.right:
                    final_list.append(curr_str)
                else:
                    helper(root.left, final_list, curr_str)
                    helper(root.right, final_list, curr_str)

                return final_list

        return helper(root)