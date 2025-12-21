from typing import List
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        li = []
        l = r = 0

        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                li.append(nums[q[0]])
                l += 1
            r += 1
        return li


sol = Solution()
print(sol.maxSlidingWindow([1, 2, 1, 0, 4, 2, 6], 3))
print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(sol.maxSlidingWindow([1], 1))
