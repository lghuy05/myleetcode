from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def backtrack(start, currentPermutation, hashset):
            if start == n:
                result.append(currentPermutation[:])
                return
            for end in range(n):
                if nums[end] in hashset:
                    continue
                new_set = hashset.copy()
                new_set.add(nums[end])
                backtrack(start + 1, currentPermutation + [nums[end]], new_set)
        backtrack(0, [], set())
        return result

sol = Solution()
print(sol.permute([1,2,3]))
        
