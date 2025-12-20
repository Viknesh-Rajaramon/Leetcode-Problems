from typing import List
from collections import defaultdict, Counter
from math import inf

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n, slopes, mids = len(points), defaultdict(list), defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dx, dy = x1 - x2, y1 - y2

                if x1 == x2:
                    k, b = inf, x1
                else:
                    k, b = (y2 - y1) / (x2 - x1), (y1 * dx - x1 * dy) / dx
                
                mid = (x1 + x2) * 10000 + (y1 + y2)
                slopes[k].append(b)
                mids[mid].append(k)
        
        result = 0
        for s in slopes.values():
            if len(s) == 1:
                continue
            
            total_sum = 0
            for c in Counter(s).values():
                result += total_sum * c
                total_sum += c
            
        for m in mids.values():
            if len(m) == 1:
                continue
            
            total_sum = 0
            for c in Counter(m).values():
                result -= total_sum * c
                total_sum += c

        return result
