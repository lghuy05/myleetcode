from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        intuition:
        for each node:
            if they are not visited:
                components += 1
            traverse
        TC: O(n+E), SP: O(n+E)
        """

        visited = set()
        components = 0
        hash = {i: [] for i in range(n)}
        for i, j in edges:
            hash[i].append(j)
            hash[j].append(i)

        def dfs(node, parent):
            if node not in visited:
                visited.add(node)
            for nei in hash[node]:
                if nei == parent or nei in visited:
                    continue
                visited.add(nei)
                dfs(nei, node)

        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i, -1)
        return components


sol = Solution()
print(sol.countComponents(5, [[0, 1], [1, 2], [3, 4]]))
print(sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
