from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # O(n)Time complexity, O(n) space
        n = len(nums)
        total = n * (n + 1) // 2
        duplicate = -1
        hash = set()
        for i in nums:
            if i in hash:
                duplicate = i
                break
            hash.add(i)
        return [duplicate, total - (sum(nums) - duplicate)]


sol = Solution()
print(sol.findErrorNums([1, 2, 2, 4]))
