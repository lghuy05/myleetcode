from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        min_result = float("inf")
        nums.sort()
        n = len(nums)
        i = 0
        while i + k <= n:
            min_result = min(min_result, nums[i + k - 1] - nums[i])
            i += 1
        return min_result
