# PROBLEM STATEMENT
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Serialization is the process of converting a data structure or object into a sequence of bits so that it
# can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed
# later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be
# serialized to a string and this string can be deserialized to the original tree structure.
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
# You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.serializePreorder(root)

    def deserialize(self, data) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.deserializePreorder(data)

    # Time Complexity: O(n) where n is the size of the tree
    # Space Complexity: O(n)
    def serializePreorder(self, root: TreeNode) -> str:
        def dfs(root: TreeNode, l: List[str] = []):
            if not root:
                l.append('N')
                return l
            else:
                l.append(str(root.val))
                dfs(root.left, l)
                dfs(root.right, l)
                return l

        return ','.join(dfs(root))

    # Time Complexity: O(n) where n is the size of the tree
    # Space Complexity: O(n)
    def deserializePreorder(self, data) -> Optional[TreeNode]:
        def dfs(l: List[str], index: List[int] = [0]) -> Optional[TreeNode]:
            if not l or index[0] >= len(l) or l[index[0]] == 'N':
                return None
            else:
                node = TreeNode(int(l[index[0]]))
                index[0] += 1
                node.left = dfs(l, index)
                index[0] += 1
                node.right = dfs(l, index)

                return node

        return dfs(data.split(','))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))