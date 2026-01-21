from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        put all the border cell if = 'O' into queue 
        start traversing, if that region doesnt satisfy, track all it coordinate
        generate a mxn grid with all 'X', then turn tracked region cell to 'O'
        """ 
        rows = len(board)
        cols = len(board[0])
        queue = deque([])
        visited = set()
        border_row = [(0, i) for i in range(cols)]+[(rows-1,i) for i in range(cols)]
        border_col = [(i,0) for i in range(1, rows-1)] + [(i, cols-1) for i in range(1, rows-1)]
        for i,j in border_row:
            if board[i][j] == 'O':
                queue.append((i,j))
                visited.add((i,j))

        for i,j in border_col:
            if board[i][j] == 'O':
                queue.append((i,j))
                visited.add((i,j))

        while queue:
            row, col = queue.popleft()
            for nr, nc in [(1,0), (0,1), (-1,0), (0,-1)]:
                newrow = row + nr
                newcol = col + nc
                if 0 <= newrow < rows and 0 <= newcol < cols and (newrow,newcol) not in visited and board[newrow][newcol] == 'O':
                    queue.append((newrow,newcol))
                    visited.add((newrow,newcol))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'
        return board
sol = Solution()
print(sol.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
