from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs(row, col, max_area):
            queue = deque()
            queue.append((row, col))
            count = 1
            visited.add((row, col))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            while queue:
                row, col = queue.popleft()
                for r, c in directions:
                    new_row = row + r
                    new_col = col + c
                    if (
                        new_row in range(rows)
                        and new_col in range(cols)
                        and (new_row, new_col) not in visited
                        and grid[new_row][new_col] == 1
                    ):
                        count += 1
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))

            max_area = max(max_area, count)
            return max_area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = bfs(i, j, max_area)
        return max_area


sol = Solution()
print(
    sol.maxAreaOfIsland(
        [[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]]
    )
)
