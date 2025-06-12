from imports import *

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()

        result = 0
        for col in zip(*grid):
            result += max(col)
        
        return result
