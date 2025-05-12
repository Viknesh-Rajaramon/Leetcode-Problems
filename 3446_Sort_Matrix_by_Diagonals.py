from imports import *

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagnol = {}
        
        for i in range(n):
            for j in range(n):
                diff = i-j
                if diff not in diagnol:
                    diagnol[diff] = []
                
                diagnol[diff].append(grid[i][j])
        
        
        for diff in diagnol.keys():
            if diff < 0:
                diagnol[diff].sort()
            else:
                diagnol[diff].sort(reverse = True)
            
        for i in range(n):
            for j in range(n):
                grid[i][j] = diagnol[i-j].pop(0)
        
        return grid
