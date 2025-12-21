from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        left = 0
        right = 1
        max_profit = 0
        n = len(prices)
        while right < n:
            if prices[right] < prices[left]:
                left = right
            else:
                max_profit = max(max_profit, prices[right] - prices[left])
            right += 1
        return max_profit


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
print(sol.maxProfit([7, 6, 4, 3, 1]))
print(sol.maxProfit([5, 1, 5, 6, 7, 8]))
print(sol.maxProfit([2, 1, 2, 1, 0, 1, 2]))
