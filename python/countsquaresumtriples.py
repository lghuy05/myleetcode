class Solution:
    def countTriples(self, n: int) -> int:
        # brute force O(n*n)
        result = 0
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                c = (i**2 + j**2) ** 0.5
                if c == int(c) and c <= n:
                    if i == j:
                        result += 1
                    else:
                        result += 2
        return result


sol = Solution()
print(sol.countTriples(10))
