from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        li: List[str] = []
        ini: List = [(0, 0, "")]
        while ini:
            open_count, close_count, current = ini.pop()
            if open_count == n and close_count == n:
                li.append(current)
                continue
            if open_count < n:
                ini.append((open_count + 1, close_count, current + "("))
            if close_count < open_count:
                ini.append((open_count, close_count + 1, current + ")"))

        return li


sol = Solution()
print(sol.generateParenthesis(3))
