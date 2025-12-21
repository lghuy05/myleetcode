from re import L
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        li = []
        # this solution is O(log(n))
        # for i in matrix:
        #     li.extend(i)
        # left, right = 0, len(li) - 1
        # while left <= right:
        #     mid = left - (right - left) // 2
        #     if li[mid] == target:
        #         return True
        #     elif li[mid] > target:
        #         left = mid + 1
        #     elif li[mid] < target:
        #         right = mid - 1
        # return False

        # O(log(m*n)) solution
        # identify row
        left, right = 0, len(matrix) - 1
        waiting = 0
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                waiting = mid
                break
            elif matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1

        li = matrix[waiting]
        left, right = 0, len(li) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == li[mid]:
                return True
            elif target < li[mid]:
                right = mid - 1
            elif target > li[mid]:
                left = mid + 1
        return False


sol = Solution()
print(sol.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10))
