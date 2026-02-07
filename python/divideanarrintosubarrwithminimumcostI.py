from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        """
        TC: O(n), SP: O(1)
        """
        n = len(nums)
        min1 = 51
        min2 = 51
        for i in range(1, n):
            if nums[i] < min1:
                min2 = min1
                min1 = nums[i]
            elif nums[i] < min2:
                min2 = nums[i]
        return nums[0] + min1 + min2


sol = Solution()
print(sol.minimumCost([1, 2, 3, 12]))
print(sol.minimumCost([5, 4, 3]))
