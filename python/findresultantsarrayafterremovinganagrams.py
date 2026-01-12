from typing import List
from collections import Counter

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        #brute force
        '''
        pseudo code
        for loop to store key value as index and Counter(index) in hash
        while loop to compare and pop matched Counter
        '''
        # n = len(words)
        # hashmap = {}
        # for i in words:
        #     hashmap[i] = Counter(i)
        #
        # while True:
        #     if len(words) < 2:
        #         break
        #     for i in range(1, len(words)):
        #         if hashmap[words[i]] == hashmap[words[i-1]]:
        #             words.pop(i)
        #             break
        #     else:
        #         break
        # return words
        '''
        optimal solution
        as because for every anagram we keep i-1
        so the least index value will always be kept
        '''

        result = [words[0]]
        n = len(words)
        hash = [Counter(w) for w in words]
        for i in range(1, n):
            if hash[i-1] != hash[i]:
                result.append(words[i])
        return result







sol = Solution()
print(sol.removeAnagrams(["abba","baba","bbaa","cd","cd"]))
        
