from typing import List


class Solution:
    # problem 1
    def sortByReflection(self, nums: List[int]) -> List[int]:
        # ©leetcode
        # O(nlogn)
        li = [bin(i)[2:] for i in nums]
        li2 = [i[::-1] for i in li]
        li3 = [int(i, 2) for i in li2]
        a = sorted(zip(li3, nums))
        return [num for _, num in a]

    # problem 2
    def largestPrime(self, n: int) -> int:
        # ©leetcode
        # O(nlog(logn))
        if n < 2:
            return 0
        is_prime = [True] * (n + 1)
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        primes = [i for i in range(2, n + 1) if is_prime[i]]
        a = 0
        b = 0
        for p in primes:
            a += p
            if a > n:
                break
            if is_prime[a]:
                b = a
        return b

    # problem 3
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        # O(n) Time complexity
        n = len(damage)
        total = 0

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + damage[i]

        for i in range(n):
            t = prefix[i + 1] - (hp - requirement[i])

            left, right = 0, i + 1
            while left < right:
                mid = (left + right) // 2
                if prefix[mid] >= t:
                    right = mid
                else:
                    left = mid + 1

            count = i + 1 - left
            total += count
        return total


sol = Solution()
# test case 1
# print(sol.sortByReflection([4, 5, 4]))
# print(sol.sortByReflection([8, 3, 6, 5]))

# test case 2
# print(sol.largestPrime(20))

# test case 3
print(sol.totalScore(11, [3, 6, 7], [4, 2, 5]))
