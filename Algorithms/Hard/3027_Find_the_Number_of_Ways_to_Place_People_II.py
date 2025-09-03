from imports import *

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key = lambda x: (x[0], -x[1]))
        
        result = 0
        for i in range(n-1):
            bottom = -inf
            for j in range(i+1, n):
                if bottom < points[j][1] <= points[i][1]:
                    result += 1
                    bottom = points[j][1]
                    if bottom == points[i][1]:
                        break
                        
        return result
