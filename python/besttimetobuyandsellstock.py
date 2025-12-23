from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # pattern I see:
        # 1 <  n < 10**5
        # brute force solution is n**2 where for each i we comparing prices[i] with prices[j] where j go from i to n
        # consider two pointers
        # TC: O(n), SC: O(1)
        left, right = 0, 1
        n = len(prices)
        result = 0
        while right < n:
            if prices[right] > prices[left]:
                result = max(result, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return result


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
print(sol.maxProfit([7, 6, 4, 3, 1]))
print(sol.maxProfit([5, 1, 5, 6, 7, 8]))
print(sol.maxProfit([2, 1, 2, 1, 0, 1, 2]))
