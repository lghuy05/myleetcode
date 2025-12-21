from re import S
from typing import List


class Solution:
    # problem 1
    def absDifference(self, nums: List[int], k: int) -> int:
        k_max = sorted(nums)[:k]
        k_min = sorted(nums, reverse=True)[:k]
        return abs(sum(k_max) - sum(k_min))

    # problem 2
    def reverseWords(self, s: str) -> str:
        li = s.split()
        vowel = {"u", "e", "o", "a", "i"}
        count = 0
        for i in li[0]:
            if i in vowel:
                count += 1
        for i in range(1, len(li)):
            letter_count = 0
            for char in li[i]:
                if char in vowel:
                    letter_count += 1
            if letter_count == count:
                li[i] = li[i][::-1]
        return " ".join(li)

    # problem 3
    def minMoves(self, balance: List[int]) -> int:
        if sum(balance) < 0:
            return -1
        n = len(balance)
        neg = -1
        need = 0
        for i in range(n):
            if balance[i] < 0:
                neg = i
                need = -balance[i]
                break

        li = balance[:]
        li_2 = []
        for i in range(n):
            if i == neg:
                continue
            dist = min(abs(i - neg), n - abs(i - neg))
            li_2.append((dist, balance[i], i))
        li_2.sort()
        result = 0
        for dist, amt, indx in li_2:
            if need == 0:
                break
            take = min(amt, need)
            result += take * dist
            need -= take
        return result


sol = Solution()
# testcase1
# print(sol.absDifference([5, 2, 2, 4], 2))
# testcase2
print(sol.reverseWords("cat and mice"))
