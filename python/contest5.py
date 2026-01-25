from typing import List


class Solution:
    def specialNodes(
        self, n: int, edges: List[List[int]], x: int, y: int, z: int
    ) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        arr = [[0, 0, 0] for _ in range(n)]

        def bfs(start, idx):
            q = deque([start])
            visited = [False] * n
            visited[start] = True
            while q:
                u = q.popleft()
                for v in g[u]:
                    if not visited[v]:
                        visited[v] = True
                        arr[v][idx] = arr[u][idx] + 1
                        q.append(v)

        bfs(x, 0)
        bfs(y, 1)
        bfs(z, 2)

        res = 0
        for i in range(n):
            a, b, c = arr[i]
            mx = max(a, b, c)
            if a * a + b * b + c * c - mx * mx == mx * mx:
                res += 1

        return res


sol = Solution()
# problem 1
# print(sol.minimumPrefixLength([1, -1, 2, 3, 3, 4, 5]))
# print(sol.minimumPrefixLength([4, 3, -2, -5]))
# print(sol.minimumPrefixLength([1, 2, 3, 4]))
# problem 2
# print(sol.rotateElements([5, 4, -9, 6], 2))
# print(sol.rotateElements([1, -2, 3, -4], 3))
