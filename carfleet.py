from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result: int = 0
        n: int = len(position)
        time_li: List[int] = []
        max_time: int = 0
        cars: List[tuple] = sorted(zip(position, speed), reverse=True)
        for position, speed in cars:
            time: int = (target - position) / speed
            if time > max_time:
                result += 1
                max_time = time

        return result


sol = Solution()
print(sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
