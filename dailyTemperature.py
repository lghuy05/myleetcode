from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # stack to store indices

        for i in range(n):
            # While current temperature is warmer than temperature at top of stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
            print(result)
        return result


sol = Solution()
# Output: [1,1,4,2,1,1,0,0]
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# print(sol.dailyTemperatures([22, 21, 20]))
