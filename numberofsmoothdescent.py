from typing import List
import math


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # result = 0
        # left = 0
        # right = 1
        # n = len(prices)
        # while right < n:
        #     if prices[right] != prices[right - 1] - 1:
        #         length = right - left
        #         result += length * (length + 1) // 2
        #         left = right
        #     right += 1
        # if left != right:
        #     result += (right - left) * (right - left + 1) // 2
        # return result

        n = len(prices)
        stack = 1
        result = 1

        for i in range(1, n):
            if prices[i] == prices[i - 1] - 1:
                stack += 1
            else:
                stack = 1
            result += stack

        return result


sol = Solution()
print(sol.getDescentPeriods([3, 2, 1, 4]))
print(sol.getDescentPeriods([8, 6, 7, 7]))
print(sol.getDescentPeriods([1]))
