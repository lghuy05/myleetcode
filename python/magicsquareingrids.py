from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        result = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if self.isMagic(grid, i, j):
                    result += 1
        return result

    def isMagic(self, grid, r, c):
        if grid[r + 1][c + 1] != 5:
            return False
        # check valid
        val = set()
        for i in range(3):
            for j in range(3):
                if (
                    grid[r + i][c + j] < 1
                    or grid[r + i][c + j] > 9
                    or grid[r + i][c + j] in val
                ):
                    return False
                val.add(grid[r + i][c + j])
        # row, cols sum
        for k in range(3):
            if sum(grid[r + k][c : c + 3]) != 15:
                return False
            if sum(grid[i + r][c + k] for i in range(3)) != 15:
                return False
        # diagonal sum
        if (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2]) != 15 or (
            grid[r + 2][c] + grid[r + 1][c + 1] + grid[r][c + 2]
        ) != 15:
            return False
        return True
