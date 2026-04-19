from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        b = n*n*(n*n+1) // 2
        a = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] not in seen:
                    seen.add(grid[i][j])
                    b -= grid[i][j]
                else:
                    a = grid[i][j]
        
        return [a, b]
