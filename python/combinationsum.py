from typing import List
from collections import deque


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        n = len(candidates)
        queue = deque()
        for i in range(n):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            queue.append((i, [candidates[i]], candidates[i]))
        while queue:
            start, path, current_sum = queue.popleft()
            if current_sum == target:
                result.append(path[:])
                continue
            elif current_sum > target:
                continue

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                new_sum = current_sum + candidates[i]
                if new_sum <= target:
                    new_path = path + [candidates[i]]
                    queue.append((i, new_path, new_sum))
        return result


sol = Solution()
print(sol.combinationSum([2, 5, 6, 9], 9))
print(sol.combinationSum([3, 4, 5], 16))
print(sol.combinationSum([3], 5))
