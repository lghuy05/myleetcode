from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        li = [0] * n
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                a = stack.pop()
                li[a] = i - a
            stack.append(i)
        return li
