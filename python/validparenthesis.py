class Solution:
    def isValid(self, s: str) -> bool:
        hash = {"(": ")", "{": "}", "[": "]"}
        n = len(s)
        stack = []
        for char in s:
            if char in hash.keys():
                stack.append(char)
            else:
                if not stack:
                    return False

                if hash[stack.pop()] != char:
                    return False

        return len(stack) == 0


sol = Solution()
print(sol.isValid("[]"))
print(sol.isValid("[(])"))
print(sol.isValid("([{}])"))
