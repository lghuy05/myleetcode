from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        li = [1] * n
        prefix = 1
        for i in range(n):
            li[i] *= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n - 1, -1, -1):
            li[i] *= postfix
            postfix *= nums[i]

        return li


sol = Solution()
print(sol.productExceptSelf([1, 2, 4, 6]))
print(sol.productExceptSelf([-1, 0, 1, 2, 3]))
