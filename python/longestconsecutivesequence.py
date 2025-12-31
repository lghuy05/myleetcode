from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                streak = 1
                while current + 1 in num_set:
                    streak += 1
                    current += 1
                result = max(streak, result)
        return result


sol = Solution()
print(sol.longestConsecutive([2, 20, 4, 10, 3, 4, 5]))
