from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque([])
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        if fresh == 0:
            return 0
        min = 0
        directions = [(1,0), (0,1), (-1,0),(0,-1)]

        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for r,c in directions:
                    new_row, new_col = row + r, col + c
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        q.append((new_row, new_col))
                        fresh -= 1
            min += 1
        return min if fresh == 0 else -1




