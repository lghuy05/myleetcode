from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            while queue:
                row, col = queue.popleft()
                for r, c in directions:
                    new_row = row + r
                    new_col = col + c
                    if (
                        new_row in range(rows)
                        and new_col in range(cols)
                        and grid[new_row][new_col] == "1"
                        and (new_row, new_col) not in visited
                    ):
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        return islands
