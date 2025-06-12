from imports import *

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = sorted(list(set([x for x, _ in points])))
        max_width = 0
        
        for i in range(len(x)-1):
            diff = x[i+1] - x[i]
            if diff > max_width:
                max_width = diff
        
        return max_width
