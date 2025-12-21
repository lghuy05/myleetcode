from typing import List
from collections import Counter, defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a: Counter = Counter(nums)
        li: List[int] = [i for i in a.values()]
        li.sort(reverse=True)
        li = li[:k]
        b: dict = defaultdict()
        for key, value in a.items():
            if value not in b:
                b[value] = []
            b[value].append(key)
        result: List[int] = []

        for i in li:
            result.append(b[i].pop())
        return result


sol = Solution()
# print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(sol.topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))
