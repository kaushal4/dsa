"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        og_clone = defaultdict(lambda: None)
        def dfs(node: Optional['Node']):
            if node == None:
                return None
            if og_clone[node] != None:
                return og_clone[node]
            new_node = Node(node.val)
            og_clone[node] = new_node
            children = []
            for child in node.neighbors:
                child_clone = dfs(child)
                children.append(child_clone)
            new_node.neighbors = children
            return new_node
        return dfs(node)
