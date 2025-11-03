from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        li: set = set(nums)
        if len(li) == len(nums):
            return False
        return True


sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 4, 5]))
print(sol.hasDuplicate([1, 2, 3, 3]))
