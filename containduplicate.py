from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(1)
        if len(set(nums)) == len(nums):
            return True
        return False


sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 4, 5]))
print(sol.hasDuplicate([1, 2, 3, 3]))
