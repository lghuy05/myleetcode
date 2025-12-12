import re
from typing import List
from collections import deque


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # O(n) time complextiy using stack
        # result = [[]]
        # queue = deque([([], 0)])
        # n = len(nums)
        # while queue:
        #     current, start = queue.popleft()
        #
        #     for i in range(start, n):
        #         new_cur = current + [nums[i]]
        #         result.append(new_cur)
        #         queue.append((new_cur, i + 1))
        #
        # return result
        #
        # recursion
        result = []

        def backtracking(index, path):
            if index == len(nums):
                result.append(path[:])
                return
            # taking
            path.append(nums[index])
            backtracking(index + 1, path)
            path.pop()

            # skipping
            backtracking(index + 1, path)

        backtracking(0, [])

        return result


sol = Solution()
print(sol.subsets([1, 2, 3]))
