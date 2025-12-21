from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(n) time complexity and O(n) space complexity
        # nums = set(nums)
        # n = len(nums)
        # for i in range(n + 1):
        #     if i not in nums:
        #         return i
        # return -1

        # O(nlog(n)) time complexity which is slower,  but less memory usage
        # nums.sort()
        # for i, value in enumerate(nums):
        #     if i != value:
        #         return i
        # return len(nums)

        # O(n) time complexity and O(1) space complexity
        return sum(range(len(nums) - 1)) - sum(nums)
