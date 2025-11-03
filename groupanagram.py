from typing import List, final
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash: dict = defaultdict(list)
        for s in strs:
            key: str = "".join(sorted(s))
            hash[key].append(s)

        return list(hash.values())


sol = Solution()
print(sol.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
