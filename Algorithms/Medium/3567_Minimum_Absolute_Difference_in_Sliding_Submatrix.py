from typing import List
from itertools import chain, pairwise
from sortedcontainers import SortedList

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        result = [[0] * (n+1-k) for _ in range(m+1-k)]
        if k == 1:
            return result
        
        for r in range(m+1-k):
            sub_mat = SortedList(chain(*[grid[r+i][ : k] for i in range(k)]))
            for c in range(n+1-k):
                result[r][c] = min([b-a for a, b in pairwise(sub_mat) if a != b], default=0)
            
                if c == n-k:
                    continue
                
                for i in range(k):
                    sub_mat.remove(grid[r+i][c])
                
                sub_mat.update([grid[r+i][c+k] for i in range(k)])

        return result
