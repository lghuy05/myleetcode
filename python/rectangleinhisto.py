from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        n = len(heights)
        for i, h in enumerate(heights):
            start = 0
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, (n - i) * h)
        return maxArea

        # stack: List[int] = []
        # max_area: int = 0
        # n: int = len(heights)
        # heights.append(0)
        # for i in range(n + 1):
        #     while stack and heights[stack[-1]] > heights[i]:
        #         height: int = heights[stack.pop()]
        #         if stack:
        #             base: int = i - stack[-1] - 1
        #         else:
        #             base: int = i
        #         max_area = max(max_area, base * height)
        #     stack.append(i)
        # return max_area


sol = Solution()
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))
