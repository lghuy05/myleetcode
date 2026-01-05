from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()

        def backtracking(current, start):
            result.append(current[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtracking(current, i + 1)
                current.pop()

        backtracking([], 0)
        return result
