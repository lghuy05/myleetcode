from typing import List
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        def bfs(i, j):
            q = deque([(i, j, 0)])
            visited = set([(i, j)])

            while q:
                r, c, dist = q.popleft()
                if grid[r][c] == 0:
                    return dist

                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] != -1 and
                        (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc, dist + 1))

            return float('inf')
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0 and grid[i][j] != -1:
                    grid[i][j] = bfs(i , j)


