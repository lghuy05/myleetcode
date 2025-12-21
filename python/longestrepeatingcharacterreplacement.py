from typing import List


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        li: List[int] = [0] * 26
        left: int = 0
        max_fre: int = 0
        count: int = 0
        n: int = len(s)
        for right in range(n):
            li[ord(s[right]) - ord("A")] += 1
            max_fre = max(max_fre, li[ord(s[right]) - ord("A")])

            while (right - left + 1) - max_fre > k:
                li[ord(s[left]) - ord("A")] -= 1
                left += 1

            count = max(count, right - left + 1)

        return count


sol = Solution()
print(sol.characterReplacement("AABABBA", 1))
