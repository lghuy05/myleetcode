from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # if not digits:
        #     return []
        # hashmap = {
        #         "2": ["a", "b", "c"],
        #         "3": ["d", "e", "f"],
        #         "4": ["g", "h", "i"],
        #         "5": ["j", "k", "l"],
        #         "6": ["m", "n", "o"],
        #         "7": ["p", "q", "r", "s"],
        #         "8": ["t", "u", "v"],
        #         "9": ["w", "x", "y", "z"],
        #         }
        # result = []
        # n = len(digits)
        # def backtrack(start, currentPermutation):
        #     if start == n:
        #         result.append(currentPermutation)
        #         return
        #     for i in hashmap[digits[start]]:
        #         backtrack(start + 1, currentPermutation + i)
        #
        # backtrack(0, "")
        # return result

    #space optimal
        
        if not digits:
            return []

        hashmap = {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"
                }
        result = []
        n = len(digits)
        def backtracking(start, path):
            if start == n:
                result.append("".join(path))
                return
            for char in hashmap[digits[start]]:
                path.append(char)
                backtracking(start + 1, path)
                path.pop()

        backtracking(0, [])
        return result
sol = Solution()
print(sol.letterCombinations("34"))
