from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # result: int = 0
        # n: int = len(position)
        # time_li: List[int] = []
        # max_time: int = 0
        # cars: List[tuple] = sorted(zip(position, speed), reverse=True)
        # for position, speed in cars:
        #     time: int = (target - position) / speed
        #     if time > max_time:
        #         result += 1
        #         max_time = time
        #
        # return result
        cars = sorted(zip(position, speed))  # Farthest to closest
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd

            # Remove cars from stack that this car will catch up to
            while stack and time >= stack[-1]:
                stack.pop()

            # Add this car's time to stack
            stack.append(time)

        return len(stack)


sol = Solution()
print(sol.carFleet(10, [1, 4], [3, 2]))
print(sol.carFleet(10, [4, 1, 0, 7], [2, 2, 1, 1]))
