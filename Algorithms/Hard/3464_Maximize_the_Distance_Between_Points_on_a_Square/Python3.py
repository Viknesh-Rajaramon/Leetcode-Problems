from typing import List
from bisect import bisect_left

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        one_d_points, perimeter = [], 4*side
        for x, y in points:
            if x == 0:
                one_d_points.append(y)
            elif y == side:
                one_d_points.append(side + x)
            elif x == side:
                one_d_points.append(3*side - y)
            else:
                one_d_points.append(4*side - x)
        
        one_d_points.sort()

        def check(limit: int) -> bool:
            for start in one_d_points:
                end, curr = start + perimeter - limit, start
                for _ in range(k-1):
                    idx = bisect_left(one_d_points, curr+limit)
                    if idx == len(one_d_points) or one_d_points[idx] > end:
                        break

                    curr = one_d_points[idx]
                else:
                    return True
            
            return False

        result, low, high = 0, 1, side
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                low = mid + 1
                result = mid
            else:
                high = mid - 1
        
        return result
