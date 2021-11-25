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

    def connectWithConstantSpace(self, root: 'Node') -> 'Node':
        if not root:
            return None
        else:
            parent = root
            childhead = child = None

            while parent:
                while parent:
                    if parent.left:
                        if not childhead:
                            childhead = parent.left
                        else:
                            child.next = parent.left
                        child = parent.left

                    if parent.right:
                        if not childhead:
                            childhead = parent.right
                        else:
                            child.next = parent.right
                        child = parent.right
                    parent = parent.next

                parent = childhead
                childhead = child = None

            return root