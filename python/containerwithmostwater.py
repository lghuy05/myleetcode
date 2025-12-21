from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        left, right = 0, len(heights) - 1
        while left < right:
            # while heights[left] == heights[left + 1]:
            #     left += 1
            # while heights[right] == heights[right - 1]:
            #     right -= 1

            base = right - left
            min_height = min(heights[left], heights[right])
            volumn = base * min_height

            max_vol = max(max_vol, volumn)
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        return max_vol


sol = Solution()
print(sol.maxArea([1, 7, 2, 5, 4, 7, 3, 6]))
