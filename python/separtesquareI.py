from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0.0
        min_y = float('inf')
        max_y = float('-inf')
        for x,y,length in squares:
            total_area += length * length
            min_y = min(min_y, y)
            max_y = max(max_y, y + length)

        target = total_area / 2.0
        def area_below(h):
            area = 0.0
            for x,y,length in squares:
                if h <= y:
                    continue
                elif h >= y + length:
                    area += length * length
                else:
                    area += (h - y) * length
            return area
        left, right = min_y, max_y
        eps = 1e-6
        while right - left > eps:
            mid = left + (right - left) / 2
            if area_below(mid) < target:
                left = mid
            else:
                right = mid
        return left


        
