from typing import List
from heapq import heappush, heappop

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        result, m, n = [], len(grid), len(grid[0])
        max_length = min((m-1)//2, (n-1)//2)
        
        def rhombus_sum(r: int, c: int, k: int) -> int:
            sum_ = grid[r][c]
            for i in range(1, k+1):
                r += 1
                sum_ += grid[r][c+i] + grid[r][c-i]
            
            for i in range(k-1, -1, -1):
                r += 1
                sum_ += grid[r][c+i]
                if i > 0:
                    sum_ += grid[r][c-i]
            
            return sum_
        
        for r in range(m):
            for c in range(n):
                for k in range(max_length+1):
                    if c >= k and c+k < n and r+2*k < m:
                        sum_ = rhombus_sum(r, c, k)
                        if sum_ not in set(result):
                            heappush(result, sum_)
                        
                        if len(result) > 3:
                            heappop(result)
        
        return sorted(result, reverse = True)
