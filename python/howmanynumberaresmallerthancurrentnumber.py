from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # O(n*n) time complexity and O(n*n) space
        # n = len(nums)
        # li = n * [0]
        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if nums[j] < nums[i]:
        #             count += 1
        #     li[i] = count
        # return li
        #
        # O(nlogn) time complexity and O(n) space
        new_nums = sorted(nums)
        hash = {}
        for i, v in enumerate(new_nums):
            if v not in hash:
                hash[v] = i
        li = []
        for i in nums:
            li.append(hash[i])
        return li
