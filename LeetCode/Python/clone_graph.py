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
        d  = {}
        if not node:
            return node

        def dfs(u = node):
            if u in d:
                return d[u]
            newNode = Node(u.val)
            d[u] = newNode
            for v in u.neighbors:
                d[u].neighbors.append(dfs(v))
            
            return d[u]
        
        return dfs()
        