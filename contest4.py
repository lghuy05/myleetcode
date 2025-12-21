class Solution:
    # problem 1
    def mirrorDistance(self, n: int) -> int:
        rev = int(str(n)[::-1])
        return abs(rev - n)
    #problem 2
    def minCost(self, s: str, cost: List[int]) -> int:
        total = sum(cost)
        li = [0]*26
        for char, c in zip(s, cost):
            li[ord(char)-ord['a']]  += cost

        return total = max(li)


©leetcode

sol = Solution()
print(sol.mirrorDistance(25))
