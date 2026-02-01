from re import S
from typing import List


class Solution:
    # problem 1
    def countMonobit(self, n: int) -> int:
        count = 1
        current = 1
        for i in range(1, n + 1):
            if i == current:
                count += 1
                current = current * 2 + 1
        return count

    # problem 2
    def finalElement(self, nums: List[int]) -> int:
        return max(nums[0], nums[-1])


def solve(nums):
    n = len(nums)
    if n <= 1:
        return n

    # --- Forward Pass ---
    # inc[i]: max len ending at i, last step was UP
    # dec[i]: max len ending at i, last step was DOWN
    inc = [1] * n
    dec = [1] * n

    ans = 1  # Track max length without removal

    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            inc[i] = dec[i - 1] + 1
        elif nums[i] < nums[i - 1]:
            dec[i] = inc[i - 1] + 1
        ans = max(ans, inc[i], dec[i])

    # --- Backward Pass ---
    # r_inc[i]: max len starting at i, next step is UP (nums[i] < nums[i+1])
    # r_dec[i]: max len starting at i, next step is DOWN (nums[i] > nums[i+1])
    r_inc = [1] * n
    r_dec = [1] * n

    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            r_inc[i] = r_dec[i + 1] + 1
        elif nums[i] > nums[i + 1]:
            r_dec[i] = r_inc[i + 1] + 1

    # --- Check Removals ---
    for i in range(1, n - 1):
        # If we remove i, we check connection between i-1 and i+1

        # Scenario 1: The connection is an UP step (i-1 < i+1)
        # The left side must have ended with DOWN (dec[i-1])
        # The right side must start with DOWN (r_dec[i+1]) to maintain pattern
        if nums[i - 1] < nums[i + 1]:
            ans = max(ans, dec[i - 1] + r_dec[i + 1])

        # Scenario 2: The connection is a DOWN step (i-1 > i+1)
        # The left side must have ended with UP (inc[i-1])
        # The right side must start with UP (r_inc[i+1])
        if nums[i - 1] > nums[i + 1]:
            ans = max(ans, inc[i - 1] + r_inc[i + 1])

    return ans


sol = Solution()
# testcase 1
# print(sol.countMonobit(4))
# testcase 2
print(sol.finalElement([3, 7]))
