from re import L
from typing import List
import bisect


class Solution:
    # problem 1
    def countElements(self, nums: List[int], k: int) -> int:
        # brute force
        # sort
        # for each element in sorted List
        # O(nlogn) for sort
        # nums.sort()
        # n = len(nums)
        # count = 0
        #
        # for x in nums:
        #     greater_count = 0
        #     for y in nums:
        #         if y > x:
        #             greater_count += 1
        #     if greater_count >= k:
        #         count += 1
        #
        # return count

        # optimize
        # nums.sort()
        # n = len(nums)
        # count = 0
        # for i in range(n):
        #     if n - i - 1 >= k:
        #         count += 1
        # return count
        #
        # O(nlogn)
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n):
            last = bisect.bisect_right(nums, nums[i])
            strictly_greater = n - last
            if strictly_greater >= k:
                count += 1

        return count

    # problem 2
    def maxDistinct(self, s: str) -> int:
        # substring as short as possbile when we make different substring
        # ensure character hasnt been used
        # O(n) time complextiy
        # greedy?
        hash = set()
        count = 0
        for ch in s:
            if ch not in hash:
                count += 1
                hash.add(ch)

        return count

    # problem 3
    # brute force

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # def reverse_num(x):
        #     return int(str(x)[::-1])

        # brute force O(n*n)
        # check all pairs (i, j ) where i < j and see if they form mirror
        # if reverse(nums[i]) == nums[j] = > mirror pair
        # track smallest j - i
        # edge case: ? no mirror pair return -1
        # min_dist = float("inf")
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if reverse_num(nums[i]) == nums[j]:
        #             min_dist = min(min_dist, j - i)
        # if min_dist != float("inf"):
        #     return min_dist
        # return -1
        #

        # optimizing
        # ini: using dict to store if current number is already being reversed
        # O(n) time complextiy
        min_dist = float("inf")
        hash = {}
        for i, v in enumerate(nums):
            rev = int(str(v)[::-1])
            if v in hash and hash[v] < i:
                min_dist = min(min_dist, i - hash[v])
                hash[v] = i
            hash[rev] = i
        return min_dist if min_dist != float("inf") else -1

    # problem 4
    def minOperations(
        self, nums: List[int], k: int, queries: List[List[int]]
    ) -> List[int]:
        #       #bruteforce O(m*nlogn)
        #       #list slicing from l to r, subarray
        #
        #       #check if all elements have same remainder mod k
        #       #(x-remainder)/k
        #       #sort
        #       #median
        #       #caculate total operations
        #       not efficient
        li = []
        for l, r in queries:
            subarr = nums[l : r + 1]
            remainder = subarr[0] % k
            uh = all((x % k) == remainder for x in subarr)
            if not uh:
                li.append(-1)
                continue

            lmao = [(x - remainder) // k for x in subarr]
            lmao.sort()
            n = len(lmao)
            median = lmao[n // 2]
            operations = sum(abs(bruh - median) for bruh in lmao)
            li.append(operations)
        return li
        # optimize
        # possible improvement
        # preprocess for each possible remainder modulo k
        # for each remainder r, maintain:
        # sorted list where nums[i] % k == r
        # prefix sum? b = (nums[i] - r) / k values for these indices
        # each query [l, r]:
        # check if all elements in range have same remainder
        # if yes, get the b values in that range from the sorted list for that remainder
        # use binary search + prefix sum to compute median and sum abs differences
        # O(logn)


# testcase 1
sol = Solution()
# print(sol.countElements([3, 1, 2], 1))
# print(sol.countElements([5, 5, 5], 2))

# testcase 2
# print(sol.maxDistinct("abab"))
# print(sol.maxDistinct("abcd"))
# print(sol.maxDistinct("aaaa"))
#
# # testcase 3
print(sol.minMirrorPairDistance([12, 21, 45, 33, 54]))
print(sol.minMirrorPairDistance([120, 21]))
print(sol.minMirrorPairDistance([21, 120]))
print(sol.minMirrorPairDistance([1000, 100, 10, 1, 100, 10, 1]))
# testcase 4
# print(sol.minOperations([1, 4, 7], 3, [[0, 1], [0, 2]]))
# print(sol.minOperations([1, 2, 4], 2, [[0, 2], [0, 0], [1, 2]]))
