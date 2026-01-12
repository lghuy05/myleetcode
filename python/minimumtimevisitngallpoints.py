from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # O(n) time complexity, O(n) space usage
        result = 0
        n = len(points)
        for i in range(1, n):
            result += max(abs(points[i][0]-points[i-1][0]),
                              abs(points[i][1]-points[i-1][1]))
        return result


sol = Solution()
print(sol.minTimeToVisitAllPoints([[3, 2], [-2, 2]]))
