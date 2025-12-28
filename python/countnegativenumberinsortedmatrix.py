from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # brute force
        # count = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] < 0:
        #             count += 1
        # return count

        # binary search over row
        # n = len(grid)
        # n_in = len(grid[0])
        # result = 0
        # for i in range(n):
        #     if grid[i][0] < 0:
        #         result += n_in
        #     else:
        #         left, right = 0, n_in - 1
        #         while left < right:
        #             mid = (right - left) // 2 + left
        #             if grid[i][mid] < 0:
        #                 right = mid - 1
        #             else:
        #                 left = mid + 1
        #         result += n_in - left
        # return result

        # sorted non-decreasing both row wise and col wise so, we start from the end of the first row
        n = len(grid)
        n_in = len(grid[0])
        result = 0
        row, col = 0, n_in - 1
        while row < n and col >= 0:
            if grid[row][col] < 0:
                result += n - row
                col -= 1
            else:
                row += 1
        return result


sol = Solution()
print(
    sol.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])
)
