class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        len_s1, len_s2 = len(s1), len(s2)
        total_ord = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
        for i in range(len_s1):
            for j in range(len_s2):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + ord(s2[j])
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return total_ord - (2 * dp[len_s1][len_s2])
