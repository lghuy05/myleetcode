from typing import List

class Solution:
    def findMinPair(self, nums) -> int:
        n = len(nums)
        min_sum = float('inf')
        index = -1
        for i in range(n-1):
            if nums[i] + nums[i+1] < min_sum:
                min_sum = nums[i] + nums[i+1]
                index = i
        return index
                
    def mergePair(self, nums, min_index) -> List[int]:
        nums[min_index] = nums[min_index] + nums[min_index +1]
        nums.pop(min_index+1)
        return nums
    def minimumPairRemoval(self, nums: List[int]) -> int:
        result = 0
        while nums != sorted(nums):
            nums = self.mergePair(nums, self.findMinPair(nums))
            result += 1
        return result

sol = Solution()
print(sol.minimumPairRemoval([5,2,3,1]))
print(sol.minimumPairRemoval([1,2,2]))
            
        
