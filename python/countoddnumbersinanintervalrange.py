class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # O(1) Time complexity, need optimization
        count = 0
        if low % 2 != 0:
            count += 1
        if high % 2 != 0:
            count += 1

        if count == 2:
            a = high - low - 1
            count += a // 2
        elif count == 1:
            a = high - low - 1
            if a == 0:
                return count
            count += a // 2
        else:
            a = high - low - 1
            if a == 0:
                return count
            count += a // 2 + 1
        return count


sol = Solution()
print(sol.countOdds(3, 7))
print(sol.countOdds(8, 10))
print(sol.countOdds(21, 22))
