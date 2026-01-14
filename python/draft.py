from typing import Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hash = {}
        q = deque([node])
        hash[node] = Node(node.val)

        while q:
            origin = q.popleft()
            for nei in origin.neighbors:
                if nei not in hash:
                    hash[nei] = Node(nei.val)
                    q.append(nei)
                    hash[origin].neighbors.append(hash[nei])
        return hash[node]


