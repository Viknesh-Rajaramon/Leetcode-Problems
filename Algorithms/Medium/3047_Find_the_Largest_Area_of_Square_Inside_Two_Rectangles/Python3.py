from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        result = 0
        for i in range(len(bottomLeft)):
            if min(topRight[i][0]-bottomLeft[i][0], topRight[i][1]-bottomLeft[i][1]) <= result:
                continue
            
            for j in range(i):
                if min(topRight[j][0]-bottomLeft[j][0], topRight[j][1]-bottomLeft[j][1]) <= result:
                    continue

                if bottomLeft[j][0] >= topRight[i][0] or bottomLeft[i][0] >= topRight[j][0]:
                    continue
                
                if bottomLeft[j][1] >= topRight[i][1] or bottomLeft[i][1] >= topRight[j][1]:
                    continue
                
                a = min(topRight[i][0], topRight[j][0]) - max(bottomLeft[i][0], bottomLeft[j][0])
                b = min(topRight[i][1], topRight[j][1]) - max(bottomLeft[i][1], bottomLeft[j][1])
                result = max(result, min(a, b))

        return result**2
