from re import L
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left: int = 0
        right: int = m * n - 1
        while left <= right:
            mid: int = left + (right - left) // 2
            row: int = mid // n
            col: int = mid % n
            if matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] == target:
                return True
        return False


sol = Solution()
print(sol.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10))
