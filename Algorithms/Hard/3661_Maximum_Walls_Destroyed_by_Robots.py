from imports import *

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        def count(a, b):
            if a > b:
                return 0

            return bisect_right(walls, b) - bisect_left(walls, a)

        coords = sorted(zip(robots, distance)) + [[inf, 0]]
        walls.sort()

        avail, result = 0, count(coords[0][0] - coords[0][1], coords[0][0] - 1)
        for i in range(len(coords) - 1):
            l, dl = coords[i]
            r, dr = coords[i+1]

            l1, r1 = l+1, min(l+dl, r-1)
            l2, r2 = max(r-dr, l+1), r-1
            
            left, right = count(l1, r1), count(l2, r2)
            both = left + right - count(max(l1, l2), min(r1, r2))

            new_avail = max(avail+left, result)
            new_used = max(avail+both, result+right)
            avail, result = new_avail, new_used

        for x in set(x for x, _ in coords):
            result += count(x, x)
            
        return result
