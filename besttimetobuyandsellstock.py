from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        left: int = 0
        right: int = 1
        max_profit = 0
        n: int = len(prices)
        while right < n:
            if prices[right] < prices[left]:
                left = right
            else:
                current = prices[right] - prices[left]
                max_profit = max(max_profit, current)
            right += 1
        return max_profit


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
print(sol.maxProfit([7, 6, 4, 3, 1]))
print(sol.maxProfit([5, 1, 5, 6, 7, 8]))
print(sol.maxProfit([2, 1, 2, 1, 0, 1, 2]))
