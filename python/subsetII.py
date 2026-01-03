from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()

        def backtracking(current, start):
            for i in range(start, n):
                result.append(current[:])
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtracking(current, i + 1)
                current.pop()

        backtracking([], 0)
        return result
