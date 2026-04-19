from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len, count = 0, 0
        for l, w in rectangles:
            s = min(l, w)
            if s > max_len:
                max_len = s
                count = 1
            elif s == max_len:
                count += 1
        
        return count
