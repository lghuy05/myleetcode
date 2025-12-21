from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_for_s: dict = defaultdict(int)
        hash_for_t: dict = defaultdict(int)
        for i in s:
            if i not in hash_for_s:
                hash_for_s[i] = 1
            else:
                hash_for_s[i] += 1

        for i in t:
            if i not in hash_for_s:
                hash_for_t[i] = 1
            else:
                hash_for_t[i] += 1
        if hash_for_s == hash_for_t:
            return True
        return False


sol = Solution()
print(sol.isAnagram("racecar", "carrace"))

