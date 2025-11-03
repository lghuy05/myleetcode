from typing import List


# class Solution:
#     def twoSum(self, ques: List[int], target: int):
#         li: List[int] = []
#         n: int = len(ques)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if target - ques[i] == ques[j]:
#                     return [i, j]
#
#         return []
#
#
# sol = Solution()
# print(sol.twoSum([1, 2, 3, 4, 5], 7))  # 1, 4


def twoSum(nums: List[int], target: int):
    hash: dict = {}
    n: int = len(nums)
    for i in range(n):
        if not hash:
            hash[nums[i]] = i
        else:
            aim: int = target - nums[i]
            if aim in hash:
                return [hash[aim], i]
        hash[nums[i]] = i
    return []


print(twoSum([1, 2, 3, 4, 5], 7))
