from imports import *

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def find(i: int, j: int, curr: int) -> int:
            if i >= m or j >= n:
                return -inf
            
            score, cost = 0, 0
            if grid[i][j] == 1:
                score, cost = 1, 1
            
            if grid[i][j] == 2:
                score, cost = 2, 1
            
            if curr + cost > k:
                return -inf
            
            if i == m-1 and j == n-1:
                if curr <= k:
                    return score
                
                return -inf
            
            return max(find(i+1, j, curr+cost), find(i, j+1, curr+cost)) + score
        
        result = find(0, 0, 0)
        return result if result != -inf else -1
