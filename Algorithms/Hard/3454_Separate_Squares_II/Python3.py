from typing import List, Tuple
from math import inf

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def union_len(intervals: List[Tuple[int, int]]) -> int:
            intervals.sort()
            res, end = 0, -inf
            for a, b in intervals:
                if a > end:
                    res += b-a
                    end = b
                elif b > end:
                    res += b-end
                    end = b

            return res
        
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x+l))
            events.append((y+l, -1, x, x+l))
        
        events.sort()
        xs, prev_y, total_area, areas = [], events[0][0], 0, []
        for y, typ, xl, xr in events:
            h = y - prev_y
            if h > 0 and xs:
                w = union_len(xs)
                areas.append((prev_y, h, w))
                total_area += h*w

            if typ == 1:
                xs.append((xl, xr))
            else:
                xs.remove((xl, xr))
            
            prev_y = y
            
        acc, half = 0, total_area / 2
        for y, h, w in areas:
            if acc + h*w >= half:
                break
            
            acc += h*w
            
        return y + (half-acc) / w
