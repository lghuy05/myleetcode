from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash: dict = {}
        n: int = len(numbers)
        for i in range(n):
            other: int = target - numbers[i]
            if other in hash:
                return [hash[other] + 1, i + 1]
            hash[numbers[i]] = i


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
