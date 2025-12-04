from typing import List
from collections import deque


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # O(nlogn) time complexity
        # brute force
        # for i in range(len(nums)):
        #     nums[i] = nums[i] ** 2
        # nums.sort()
        # return nums

        # two lists, one for positive and one for negative, then merge
        # O(n) time complexity
        # pos_li = []
        # neg_li = deque()
        # for element in nums:
        #     if element < 0:
        #         neg_li.appendleft(element**2)
        #     else:
        #         pos_li.append(element**2)
        # i = 0
        # j = 0
        # result = []
        # while i < len(pos_li) and j < len(neg_li):
        #     if pos_li[i] <= neg_li[j]:
        #         result.append(pos_li[i])
        #         i += 1
        #     else:
        #         result.append(neg_li[j])
        #         j += 1
        # while i < len(pos_li):
        #     result.append(pos_li[i])
        #     i += 1
        # while j < len(neg_li):
        #     result.append(neg_li[j])
        #     j += 1
        # return result

        # another O(n) solution
        # ini two pointer left and right
        # loop from the end of the list, compare nums[left] and nums[right] to add to result list
        n = len(nums)
        left, right = 0, n - 1
        result = [0] * n
        for i in range(n - 1, -1, -1):
            if nums[left] ** 2 <= nums[right] ** 2:
                result[i] = nums[right] ** 2
                right -= 1
            else:
                result[i] = nums[left] ** 2
                left += 1
        return result


sol = Solution()
print(sol.sortedSquares([-4, -1, 0, 3, 10]))
