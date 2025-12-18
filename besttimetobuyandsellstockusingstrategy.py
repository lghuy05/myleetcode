from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + prices[i] * strategy[i]

        half = k // 2
        window_sum = sum(prices[half:k])
        max_profit = max(prefix_sum[n], prefix_sum[n] - prefix_sum[k] + window_sum)

        for start in range(1, n - k + 1):
            window_sum += prices[start + k - 1] - prices[start + half - 1]
            max_profit = max(
                max_profit,
                prefix_sum[n] + window_sum - prefix_sum[start + k] + prefix_sum[k],
            )
        return max_profit


sol = Solution()
print(sol.maxProfit([4, 2, 8], [-1, 0, 1], 2))
print(sol.maxProfit([5, 4, 3], [1, 1, 0], 2))
# print(sol.maxProfit([4, 7, 13], [-1, -1, 0], 2))
