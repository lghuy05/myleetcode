from typing import List
class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers) - 1
        while left < right:
            aim = target - numbers[left]
            if aim < numbers[right]:
                right -= 1
            elif aim > numbers[right]:
                left += 1
            else:
                return [left + 1,right + 1]]
        
