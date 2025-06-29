from imports import *

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        points.sort()
        x = [p[0] for p in points]

        result = []
        for xj, yj, rj in queries:
            i = bisect_left(x, xj-rj)
            j = bisect_right(x, xj+rj)

            ans = 0
            for xi, yi in points[i : j+1]:
                if (xi-xj)**2 + (yi-yj)**2 <= rj**2:
                    ans += 1
            
            result.append(ans)
        
        return result
