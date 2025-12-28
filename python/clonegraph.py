class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # dfs to traverse
        # TC: O(N + E), SC: O(N)
        # if not node:
        #     return None
        #
        # map = {}
        #
        # def dfs(node):
        #     if node in map:
        #         return map[node]
        #
        #     copy = Node(node.val)
        #     map[node] = copy
        #
        #     for nei in node.neighbors:
        #         copy.neighbors.append(dfs(nei))
        #     return copy
        #
        # return dfs(node)
        #

        # TC:O(N+C) SC: O(N+E)
        if not node:
            return None
        map = {}
        queue = deque([node])
        map[node] = Node(node.val)
        while queue:
            origin = queue.popleft()
            for nei in origin.neighbors:
                if nei not in map:
                    map[nei] = Node(nei.val)
                    queue.append(nei)
                map[origin].neighbors.append(map[nei])

        return map[node]
