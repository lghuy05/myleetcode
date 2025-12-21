class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_str: int = 0
        left: int = 0
        hash: set = set()
        n: int = len(s)
        for right in range(n):
            while s[right] in hash:
                hash.remove(s[left])
                left += 1
            hash.add(s[right])
            max_str = max(max_str, right - left + 1)
        return max_str


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
