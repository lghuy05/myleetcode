from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # O(n*n) time complexity
        visit = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                row, col = q.popleft()
                for rd, cd in directions:
                    new_row = row + rd
                    new_col = col + cd
                    if (
                        new_row in range(rows)
                        and new_col in range(cols)
                        and (new_row, new_col) not in visit
                        and grid[new_row][new_col] == "1"
                    ):
                        q.append((new_row, new_col))
                        visit.add((new_row, new_col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands
