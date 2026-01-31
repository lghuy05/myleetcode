from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        TC: O(n), SP: O(1)
        """
        i = 0
        n = len(letters)
        while i < n and ord(letters[i]) <= ord(target):
            i += 1
        return letters[i] if i != n else letters[0]


sol = Solution()
print(sol.nextGreatestLetter(["c", "f", "j"], "a"))
