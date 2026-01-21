from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        rows = len(heights)
        cols = len(heights[0])
        def bfs(r,c):
            q = deque([(r,c)])
            visited = {(r,c)}
            pacific = False
            atlantic = False
            while q:
                row, col = q.popleft()
                if row == 0 or col == 0:
                    pacific = True
                if row == rows - 1 or col == cols - 1:
                    atlantic = True
                for r, c in [(1,0), (0,1), (-1,0),(0,-1)]:
                    new_row = r + row
                    new_col = c + col
                    if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and heights[new_row][new_col] <= heights[row][col]:
                        q.append((new_row,new_col))
                        visited.add((new_row,new_col))
            return pacific and atlantic
        for i in range(rows):
            for j in range(cols):
                if bfs(i,j):
                    result.append([i,j])
        return result
        
sol = Solution()
print(sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))

