from typing import List
import math


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        # O(n)
        n = len(complexity)
        mod = 10**9 + 7
        a = complexity[0]

        for i in range(1, n):
            if complexity[i] <= a:
                return 0
        result = 1
        for i in range(1, n):
            result = result * i % mod

        return result


sol = Solution()
print(sol.countPermutations([1, 2, 3]))
print(sol.countPermutations([3, 3, 3, 4, 4, 4]))
print(sol.countPermutations([58, 283, 52]))
