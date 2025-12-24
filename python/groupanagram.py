from typing import List, final
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # i can see all the anagram is group - > which is no duplicate group allowed
        # consider hash, set - dictionary
        # choose a random word to mark that group identity is pretty easy
        # consider hashmap
        # pseudo code

        # sort the word, check if it exist in the hashmap
        # loop
        # if yes append, else create new key
        # loop over hashmap values
        # join the result
        # TC: O(n), SC: O(n)
        # n = len(strs)
        # hash = {}
        # for i in range(n):
        #     a = sorted(strs[i])
        #     a = "".join(a)
        #     if a not in hash:
        #         hash[a] = [strs[i]]
        #     else:
        #         hash[a].append(strs[i])
        # result = []
        # for i in hash.values():
        #     result.append(i)
        # return result

        # sort is fast but not optimal, we can use array to track word element count instead
        hash = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1
            hash[tuple(count)].append(s)
        return list(hash.values())


sol = Solution()
print(sol.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
