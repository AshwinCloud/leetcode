# PROBLEM STATEMENT
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
# The binary tree has the following definition:

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        return self.connectWithConstantSpace(root)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def connectWithConstantSpace(self, root: 'Node') -> 'Node':
        parent = root

        while parent:
            first_child = current_child = None
            while parent:
                if parent.left:
                    if not first_child:
                        first_child = parent.left
                    else:
                        current_child.next = parent.left

                    current_child = parent.left

                if parent.right:
                    if not first_child:
                        first_child = parent.right
                    else:
                        current_child.next = parent.right

                    current_child = parent.right

                parent = parent.next
            parent = first_child

        return root

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def connectWithQueue(self, root: 'Node') -> 'Node':
        if not root:
            return None
        else:
            queue = []
            previous_node = None
            previous_height = 0
            queue.insert(0, (root, 1))

            while queue:
                node, height = queue.pop()

                if previous_node and previous_height == height:
                    previous_node.next = node

                if node.left:
                    queue.insert(0, (node.left, height + 1))
                if node.right:
                    queue.insert(0, (node.right, height + 1))

                previous_node = node
                previous_height = height

            return root