from re import S
from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # TC: O(nlogn), SC: O(1)
        # greedy
        happiness.sort()
        result = 0
        i = 0
        while k:
            if happiness[-1] - i > 0:
                result += happiness.pop() - i
            i += 1
            k -= 1
        return result


sol = Solution()
print(sol.maximumHappinessSum([1, 2, 3], 2))
print(sol.maximumHappinessSum([1, 1, 1, 1], 2))
print(sol.maximumHappinessSum([2, 3, 4, 5], 1))
