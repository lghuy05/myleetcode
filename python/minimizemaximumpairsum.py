from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ans = float("-inf")
        nums.sort()
        n = len(nums)
        for i in range(n):
            ans = max(ans, nums[i] + nums[-i - 1])
        return ans


sol = Solution()
print(sol.minPairSum([3, 5, 2, 3]))
print(sol.minPairSum([3, 5, 4, 2, 4, 6]))
