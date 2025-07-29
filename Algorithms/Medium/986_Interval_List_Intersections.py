from imports import *

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        
        result = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            first, second = firstList[i], secondList[j]
            
            start, end = max(first[0], second[0]), min(first[1], second[1])
            if start <= end:
                result.append([start, end])

            if first[1] <= second[1]:
                i += 1
            else:
                j += 1
        
        return result
