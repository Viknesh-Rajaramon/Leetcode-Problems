from imports import *

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n):
            if sum(grid[i]) == n-1:
                return i
        
        return 0
