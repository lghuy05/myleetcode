from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: List[int] = []
        max_area: int = 0
        n: int = len(heights)
        heights.append(0)
        for i in range(n + 1):
            while stack and heights[stack[-1]] > heights[i]:
                height: int = heights[stack.pop()]
                if stack:
                    base: int = i - stack[-1] - 1
                else:
                    base: int = i
                max_area = max(max_area, base * height)
            stack.append(i)
        return max_area


sol = Solution()
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))
