from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hashmap = {i: [] for i in range(n)}
        for i, j in edges:
            hashmap[i].append(j)
            hashmap[j].append(i)
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for nei in hashmap[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                if not dfs(nei, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
        return len(visited) == n


sol = Solution()
print(sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
