from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1

        while left < right:
            mid: int = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


sol = Solution()
print(sol.findMin([3, 4, 5, 6, 1, 2]))
