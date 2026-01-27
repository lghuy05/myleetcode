from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_abs = float("inf")
        n = len(arr)
        result = []
        for i in range(n - 1):
            if abs(arr[i + 1] - arr[i]) < min_abs:
                min_abs = abs(arr[i + 1] - arr[i])
                result = []
                result.append([arr[i], arr[i + 1]])
            elif abs(arr[i + 1] - arr[i]) == min_abs:
                result.append([arr[i], arr[i + 1]])
        return result


sol = Solution()
print(sol.minimumAbsDifference([4, 2, 1, 3]))
print(sol.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))
