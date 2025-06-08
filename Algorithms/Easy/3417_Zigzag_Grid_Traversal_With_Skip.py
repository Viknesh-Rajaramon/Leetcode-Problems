from imports import *

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        result = []
        m, n = len(grid), len(grid[0])
        for row in range(m):
            temp = []
            for col in range(row % 2, n, 2):
                temp.append(grid[row][col])
            
            if row % 2:
                result.extend(temp[::-1])
            else:
                result.extend(temp)
        
        return result
