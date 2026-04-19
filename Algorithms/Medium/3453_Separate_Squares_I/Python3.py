from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        squares.sort(key = lambda x: x[1])
        max_y, total_area = 0, 0
        for _, y, l in squares:
            total_area += l*l
            max_y = max(max_y, y+l)
        
        def check(y_limit: float) -> bool:
            area = 0
            for _, y, l in squares:
                diff = y_limit-y
                if diff <= 0:
                    break
                
                area += l * min(l, diff)

            return area >= total_area/2
        
        low, high, err = 0, max_y, 1e-5
        while abs(high-low) > err:
            mid = (low+high)/2
            if check(mid):
                high = mid
            else:
                low = mid

        return high
