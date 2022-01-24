# PROBLEM STATEMENT
# https://leetcode.com/problems/clone-graph/
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.cloneGraphDFS(node)

    # Time Complexity: O(E + V) where E and V are the edges and vertices in the graph
    # Space Complexity: O(E + V)
    def cloneGraphDFS(self, node: 'Node') -> 'Node':
        def dfs(node: 'Node', oldToNewDict={}) -> 'Node':
            if node in oldToNewDict:
                return oldToNewDict[node]
            else:
                copy_node = Node(node.val)
                oldToNewDict[node] = copy_node
                for neighbor in node.neighbors:
                    copy_node.neighbors.append(dfs(neighbor, oldToNewDict))

                return oldToNewDict[node]

        return dfs(node) if node else None