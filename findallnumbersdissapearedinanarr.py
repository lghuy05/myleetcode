from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # O(n) time complexity and O(1) space
        # seen = set()
        # li = []
        # for i in range(1, (nums + 1)):
        #     if nums[i - 1] in seen:
        #         li.append([i])
        #     seen.add(i)
        # return li

        # O(n) time complexity and O(1) space complexity

        li = []
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        for i, v in enumerate(nums):
            if v > 0:
                li.append(i + 1)
        return li
