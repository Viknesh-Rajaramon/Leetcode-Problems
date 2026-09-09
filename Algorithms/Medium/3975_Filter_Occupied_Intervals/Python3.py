from typing import List

class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        occupiedIntervals.sort()
        idx = 0
        for i in range(1, len(occupiedIntervals)):
            if occupiedIntervals[i][0] <= occupiedIntervals[idx][1]+1:
                occupiedIntervals[idx][1] = max(occupiedIntervals[idx][1], occupiedIntervals[i][1])
            else:
                idx += 1
                occupiedIntervals[idx] = occupiedIntervals[i]
        
        result = []
        for i in range(idx+1):
            start, end = occupiedIntervals[i]
            if end < freeStart or start > freeEnd:
                result.append([start, end])
            
            if start < freeStart and end >= freeStart:
                result.append([start, freeStart-1])
            
            if start <= freeEnd and end > freeEnd:
                result.append([freeEnd+1, end])

        return result
