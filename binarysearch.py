from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index: int = -1
        left: int = 0
        right: int = len(nums) - 1
        while left <= right:
            mid: int = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                return mid
        return index


sol = Solution()
print(sol.search([-1, 0, 2, 4, 6, 8], 4))
