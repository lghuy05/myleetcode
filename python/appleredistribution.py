from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # We need to find minimum boxes that still can store all the apple
        # we only need the remain = capacities - apples and take out as much box as possible to clear the remain

        # TC: O(nlogn), SC: O(1)
        # total_apple = sum(apple)
        # total_capacity = sum(capacity)
        # count = 0
        # capacity.sort()
        # if total_apple > total_capacity:
        #     return 0
        # remain = total_capacity - total_apple
        # i = 0
        # while capacity[i] <= remain:
        #     remain -= capacity[i]
        #     count += 1
        #     i += 1
        # return len(capacity) - count
        #

        capacity.sort(reverse=True)
        used = 0
        total = 0
        total_apple = sum(apple)
        for c in capacity:
            total += c
            used += 1
            if total >= total_apple:
                return used


sol = Solution()
print(sol.minimumBoxes([1, 3, 2], [4, 3, 1, 5, 2]))
print(sol.minimumBoxes([5, 5, 5], [2, 4, 2, 7]))
print(sol.minimumBoxes([9, 8, 8, 2, 3, 1, 6], [10, 1, 4, 10, 8, 5]))
