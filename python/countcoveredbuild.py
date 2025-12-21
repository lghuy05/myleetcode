from re import S
import re
from types import resolve_bases
from typing import List
from collections import defaultdict


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # min_x = float("inf")
        # max_x = float("-inf")
        # min_y = float("inf")
        # max_y = float("-inf")
        # result = 0
        # hash_x = {}
        # hash_y = {}
        # for i in buildings:
        #     if i[0] < min_x:
        #         min_x = i[0]
        #     if i[0] > max_x:
        #         max_x = i[0]
        #
        #     if i[1] < min_y:
        #         min_y = i[1]
        #     if i[1] > max_y:
        #         max_y = i[1]
        #
        #     hash_x[i[0]] = i[1]
        #     hash_y[i[1]] = i[0]
        #
        # for i in buildings:
        #     if (
        #         min_x < i[0] < max_x
        #         and min_y < i[1] < max_y
        #         and hash_x[min_x] == i[1] == hash_x[max_x]
        #         and hash_y[min_y] == i[0] == hash_y[max_y]
        #     ):
        #         result += 1
        # return result
        #
        # O(n) Time Complexity
        result = 0
        min_x = defaultdict(lambda: float("inf"))
        max_x = defaultdict(lambda: float("-inf"))
        min_y = defaultdict(lambda: float("inf"))
        max_y = defaultdict(lambda: float("-inf"))
        for x, y in buildings:
            if min_x[y] > x:
                min_x[y] = x
            if max_x[y] < x:
                max_x[y] = x
            if min_y[x] > y:
                min_y[x] = y
            if max_y[x] < y:
                max_y[x] = y

        for x, y in buildings:
            have_below = y < max_y[x]
            have_above = y > min_y[x]
            have_right = x > min_x[y]
            have_left = x < max_x[y]
            if have_above and have_below and have_left and have_right:
                result += 1
        return result


sol = Solution()
print(sol.countCoveredBuildings(3, [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]))
print(sol.countCoveredBuildings(5, [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]))
print(sol.countCoveredBuildings(3, [[1, 1], [1, 2], [2, 1], [2, 2]]))
