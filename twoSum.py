from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) time complexity and O(n) space usage
        # n = len(nums)
        # hash = {}
        # for i in range(n):
        #     remain = target - nums[i]
        #     if remain in hash:
        #         return [hash[remain], i]
        #     hash[nums[i]] = i

        # O(n*n) time complexity and O(1) space
        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         remain = target - nums[i]
        #         if remain == nums[j]:
        #             return [i, j]

        # O(n) time complexity and O(n) space usage
        hash = {}
        for i, v in enumerate(nums):
            if target - v in hash:
                return [i, hash[target - v]]
            hash[v] = i


sol = Solution()
print(sol.twoSum([1, 2, 3, 4, 5], 7))
