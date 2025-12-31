from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = self.calculate_prefixsum(nums)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right + 1]
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

    def calculate_prefixsum(self, nums):
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        return prefix_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
#
testcase = NumArray([-2, 0, 3, -5, 2, -1])
print(testcase.prefix_sum)
print(testcase.sumRange(0, 2))
print(testcase.sumRange(2, 5))
print(testcase.sumRange(0, 5))
