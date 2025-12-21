class Solution:
    def beautySum(self, s: str) -> int:
        # O(n*n*26) time complexity
        result = 0
        for i in range(len(s)):
            li = [0] * 26
            for j in range(i, len(s)):
                li[ord(s[j]) - ord("a")] += 1
                max_count = 0
                min_count = float("inf")
                for count in li:
                    if count > 0:
                        # max_count = max(max_count, count)
                        # min_count = min(min_count, count)
                        if count > max_count:
                            max_count = count
                        if count < min_count:
                            min_count = count

                result += max_count - min_count
        return result


sol = Solution()
print(sol.beautySum("aabcb"))
print(sol.beautySum("aabcbaa"))
