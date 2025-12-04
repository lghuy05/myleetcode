from typing import List
import math
from collections import Counter


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # loop -> store in groups that have same y coordinate -> parrel to x axis
        # store in dictionary key - value <=> y - [points]
        # loop again to find how many way to grab to points from a group
        # total ways = * all possible way
        total = 1
        hash = {}
        for point in points:
            if point[1] not in hash:
                hash[point[1]] = [[point]]
            else:
                hash[point[1]].append(point)
        li = []
        for way in hash.values():
            if len(way) < 2:
                continue
            elif len(way) == 2:
                li.append(1)
                continue
            choices = int(
                math.factorial(len(way)) / (2 * math.factorial((len(way) - 2)))
            )
            li.append(choices)
        if len(li) > 1 and li[-1] > 0 and li[-2] > 0:
            for i in li:
                total *= i
            if total == 1:
                total = int(
                    math.factorial(len(li)) / (2 * math.factorial((len(li) - 2)))
                )
            return total
        return 0


sol = Solution()
print(sol.countTrapezoids([[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]))
print(sol.countTrapezoids([[0, 0], [1, 0], [0, 1], [2, 1]]))
print(sol.countTrapezoids([[87, -39], [12, -94], [-30, -11], [-76, -11]]))
print(sol.countTrapezoids([[50, -41], [64, -66], [-45, -41], [-58, 10], [25, 10]]))
print(
    sol.countTrapezoids(
        [[-73, -72], [-1, -56], [-92, 30], [-57, -89], [-19, -89], [-35, 30], [64, -72]]
    )
)
