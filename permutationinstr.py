from typing import List


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left: int = 0
        right: int = len(s1) - 1
        s1_li: List[int] = [0] * 26
        s2_li: List[int] = [0] * 26
        for i in s1:
            s1_li[ord(i) - ord("a")] += 1
        ini: str = s2[left : right + 1]
        for i in ini:
            s2_li[ord(i) - ord("a")] += 1
        if s1_li == s2_li:
            return True
        right += 1
        while right < len(s2):
            s2_li[ord(s2[right]) - ord("a")] += 1
            s2_li[ord(s2[left]) - ord("a")] -= 1
            left += 1
            if s1_li == s2_li:
                return True
            right += 1
        return False


sol = Solution()
print(sol.checkInclusion("ab", "eidbaooo"))
print(sol.checkInclusion("ab", "eidboaoo"))
