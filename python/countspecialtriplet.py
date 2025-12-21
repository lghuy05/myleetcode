from typing import List
from collections import defaultdict


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        # O(n*n*n) Time Complexity
        # result = 0
        # mod = 10 * 9 + 7
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i, n):
        #         for k in range(j, n):
        #             if nums[i] == nums[j] * 2 and nums[k] == nums[j] * 2 and i < j < k:
        #                 result += 1
        # return result % mod
        # O(n) Time Complexity, O(n) space complexity
        result = 0
        mod = 10**9 + 7
        rightHash = defaultdict(int)
        leftHash = defaultdict(int)
        n = len(nums)
        for num in nums:
            rightHash[num] += 1
        for num in nums:
            double = num * 2
            rightHash[num] -= 1
            leftCount = leftHash[double]
            rightCount = rightHash[double]
            result += leftCount * rightCount
            leftHash[num] += 1
        return result % mod


sol = Solution()
print(sol.specialTriplets([6, 3, 6]))
print(sol.specialTriplets([0, 1, 0, 0]))
print(sol.specialTriplets([8, 4, 2, 8, 4]))
