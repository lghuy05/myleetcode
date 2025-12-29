from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        hash = defaultdict(list)
        for a,b,c in allowed:
            hash[(a,b)].append(c)

        def dfs(row):
            if len(row) == 1:
                return True
            def build(i, cur):
                if i == len(row) - 1:
                    return dfs(cur)

                pair = (row[i], row[i+1])
                if pair not in hash:
                    return False
                for c in hash[pair]:
                    if build(i+1, cur + c):
                        return True
                
                return False 
            return build(0, "")
        return dfs(bottom)
