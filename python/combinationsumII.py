from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        n = len(candidates)

        def backtracking(start, current_arr, current_sum):
            if current_sum == target:
                result.append(current_arr[:])
                return

            if current_sum > target or start >= n:
                return

            for i in range(start, n):
                if start < i and candidates[i - 1] == candidates[i]:
                    continue

                if current_sum + candidates[i] > target:
                    break

                current_arr.append(candidates[i])
                backtracking(i + 1, current_arr, current_sum + candidates[i])
                current_arr.pop()

        backtracking(0, [], 0)
        return result
