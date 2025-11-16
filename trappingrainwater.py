from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        left, right = 0, len(height) - 1
        while left < right and (height[left] == 0 or height[left + 1] >= height[left]):
            left += 1
        while left < right and (
            height[right] == 0 or height[right - 1] >= height[right]
        ):
            right -= 1

        sum_vol = 0
        while left < right:
            if height[left] <= height[right]:
                pointer = left + 1
                while height[pointer] < height[left]:
                    sum_vol += height[left] - height[pointer]
                    pointer += 1
                left = pointer
            else:
                pointer = right - 1
                while height[pointer] < height[right]:
                    sum_vol += height[right] - height[pointer]
                    pointer -= 1
                right = pointer

        return sum_vol


sol = Solution()
print(sol.trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
