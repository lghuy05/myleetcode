from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hash_set = set()
        for i in nums:
            if i in hash_set:
                return i
            hash_set.add(i)
        return -1
