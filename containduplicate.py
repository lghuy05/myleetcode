from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(n) time complexity, O(n) space due to new set memory allocation
        # if len(set(nums)) == len(nums):
        #     return False
        # return True

        # O(n) time complexity, O(n) space worst scenario but more effiect due to early return if True
        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen.add(i)
        # return False

        # O(nlogn) time complexity, O(1) space complexity
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 4, 5]))
print(sol.hasDuplicate([1, 2, 3, 3]))
