# PROBLEM STATEMENT
# https://leetcode.com/problems/lru-cache/
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
# evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return f"({self.key}:{self.val})"

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def removeNode(self, node: Node):
        node.prev.next, node.next.prev = node.next, node.prev

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def addMru(self, node: Node):
        node.next, node.prev = self.mru, self.mru.prev
        self.mru.prev.next = self.mru.prev = node

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.addMru(node)
            return node.val
        else:
            return -1

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeNode(node)
            self.addMru(node)
        else:
            node = Node(key, value)
            if len(self.cache) == self.capacity:
                self.cache.pop(self.lru.next.key)
                self.removeNode(self.lru.next)

            self.cache[key] = node
            self.addMru(node)

    def printNodes(self):
        node = self.lru
        s = ""
        while node:
            # print(node)
            s += str(node) + " "
            node = node.next
        print(f"{s}")

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)