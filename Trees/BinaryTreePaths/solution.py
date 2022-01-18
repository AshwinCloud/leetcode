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
        return self.binaryTreePathsRecursive(root)

    def binaryTreePathsRecursive(self, root: Optional[TreeNode]) -> List[str]:
        def helper(curr_list: List[int], final_list: List[str], root: Optional[TreeNode]) -> List[str]:
            if not root:
                return final_list
            else:
                curr_list.append(root.val)

                if not root.left and not root.right:
                    final_list.append(setToStr(curr_list))
                elif root.left and not root.right:
                    helper(curr_list, final_list, root.left)
                elif not root.left and root.right:
                    helper(curr_list, final_list, root.right)
                else:
                    curr_list_copy = curr_list.copy()
                    helper(curr_list, final_list, root.left)
                    helper(curr_list_copy, final_list, root.right)

                return final_list

        def helper2(curr_str: str, final_list: List[str], root: Optional[TreeNode]) -> List[str]:
            if not root:
                return final_list
            else:
                if not curr_str:
                    curr_str += str(root.val)
                else:
                    curr_str += "->" + str(root.val)
                if not root.left and not root.right:
                    final_list.append(curr_str)
                elif root.left and not root.right:
                    helper2(curr_str, final_list, root.left)
                elif not root.left and root.right:
                    helper2(curr_str, final_list, root.right)
                else:
                    s1 = curr_str
                    s2 = curr_str + ""
                    helper2(s1, final_list, root.left)
                    helper2(s2, final_list, root.right)

                return final_list

        def setToStr(l: List[int]) -> str:
            if not l:
                return ""
            else:
                s = str(l[0])
                for i in range(1, len(l)):
                    s += "->" + str(l[i])
                return s

        # return helper([], [], root)
        if not root:
            return []
        else:
            return helper2("", [], root)