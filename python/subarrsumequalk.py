from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # this can easily be regconize as prefix sum
        # intuitive:
        # sum(nums[i:j]) (which is the subarray) = prefix_sum[j] - prefix_sum[i] == k
        # so prefix_sum[i] = prefix[j] - k
        # we finding possible all i index that have prefix_sum = prefix[j] - k
        # because we need to track if prefix existed on going so we need a hashmap
        # what i mean by this is because nums[] have both positive and negative integers
        # mean cancel out can happen and a prefix_sum value can appear again
        prefix_sum = 0
        count = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1  # Base case: in term prefix_sum[j] - k = 0
        for num in nums:
            prefix_sum += num
            count += hashmap[prefix_sum - k]
            hashmap[prefix_sum] += 1
        return count


sol = Solution()
print(sol.subarraySum([1, 1, 1], 2))
print(sol.subarraySum([-1, -1, 1], 1))
