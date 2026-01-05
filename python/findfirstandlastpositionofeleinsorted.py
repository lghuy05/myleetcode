from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        if not nums:
            return [-1, -1]

        def searchFirst():
            left, right = 0, len(nums) - 1
            found = False
            while left <= right:
                mid = (right - left) // 2 + left
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    right = mid - 1
                    found = True
            if found:
                return left
            return -1

        def searchLast():
            left, right = 0, len(nums) - 1
            found = False
            while left <= right:
                mid = (right - left) // 2 + left
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    left = mid + 1
                    found = True
            if found:
                return right
            return -1

        result.append(searchFirst())
        result.append(searchLast())
        return result


sol = Solution()
print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
