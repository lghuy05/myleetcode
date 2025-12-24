from typing import List


class Solution:
    def missingnumber(self, arr: List[int]) -> int:
        # Calculate expected sum (sum if there is no missing number)
        # missing number = expected sum - actual sum
        # TC: O(n), SC: O(1)
        # expected_sum = 0
        # for i in range(arr[0], arr[-1] + 1):
        #     expected_sum += i
        # return expected_sum - sum(arr)
        #
        # optimize
        # ascending array -> binary search
        #
        n = len(arr)
        left, right = 0, n - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if arr[0] + mid != arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return arr[0] + left


sol = Solution()
print(sol.missingnumber([1, 2, 3, 5]))
print(sol.missingnumber([11, 12, 14, 15, 16]))
