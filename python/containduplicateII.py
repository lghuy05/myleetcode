from typing import List
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hashmap = defaultdict(int)
        for i in range(n):
            if nums[i] in hashmap:
                if abs(i - hashmap[nums[i]]) <= k:
                    return True
            hashmap[nums[i]] = i
        return False
