class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = "".join([i.lower() for i in s if i.isalnum()])
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


sol = Solution()
print(sol.isPalindrome("ABA"))
