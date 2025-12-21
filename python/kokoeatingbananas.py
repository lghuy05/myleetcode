import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        li: List[int] = []
        minimum: int = 1
        maximum: int = max(piles)
        while minimum <= maximum:
            k: int = minimum + (maximum - minimum) // 2
            result: int = 0
            for p in piles:
                result += math.ceil(p / k)
            if result > h:
                minimum = k + 1
            elif result <= h:
                maximum = k - 1
        return minimum


sol = Solution()
print(sol.minEatingSpeed([3, 6, 7, 11], 8))
