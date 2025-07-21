from imports import *

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)

        slopes = defaultdict(lambda: defaultdict(int))
        mids = defaultdict(lambda: defaultdict(int)) 

        def slope(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            g = gcd(dx, dy)
            dx //= g
            dy //= g
            
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
            
            return (dy, dx)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                s = slope(points[i], points[j])
                slopes[s][s[1] * y1 - s[0] * x1] += 1
                mids[(x1 + x2, y1 + y2)][s] += 1
        
        result = 0
        for line_counts in slopes.values():
            total = sum(line_counts.values())
            result += (total**2 - sum(v**2 for v in line_counts.values())) // 2
        
        for sCnt in mids.values():
            v = sum(sCnt.values())
            if v > 1:
                result -= v * (v-1) // 2 - sum(c * (c-1) // 2 for c in sCnt.values())

        return result
