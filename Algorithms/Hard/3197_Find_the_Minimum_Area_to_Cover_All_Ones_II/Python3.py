from typing import List
from bisect import bisect_left, bisect_right
from functools import lru_cache

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def rc(r1, r2, c1, c2):
            if r1 > r2 or c1 > c2:
                return 0
            flag = False
            rmin, rmax, = float('inf'), -1
            cmin, cmax = float('inf'), -1
            for i in range(r1,r2+1):
                r = ps[i]
                if not r:
                    continue
                k = bisect_left(r,c1)
                if k < len(r) and r[k] <= c2:
                    flag = True
                    rmin = min(rmin, i)
                    rmax = i
                    cmin = min(cmin, r[k])
                    cmax = max(cmax, r[bisect_right(r, c2)-1])
            return 0 if not flag else (rmax-rmin+1)*(cmax-cmin+1)
        
        n, m = len(grid), len(grid[0])
        ps = [[] for _ in range(n)]
        for i in range(n):
            r = ps[i]
            for j, v in enumerate(grid[i]):
                if v:
                    r.append(j)
        
        tot = rc(0, n-1, 0, m-1)
        for c in range(-1, m-1):
            tot = min(tot, rc(0, n-1, 0, c) + rc(0, n-1, c+1, m-1))
        for r in range(-1, n-1):
            tot = min(tot, rc(0, r, 0, m-1) + rc(r+1, n-1, 0, m-1))
        for c1 in range(-1, m-1):
            for c2 in range(c1, m-1):
                tot = min(tot, rc(0, n-1, 0, c1)+rc(0, n-1, c1+1, c2) + rc(0, n-1, c2+1, m-1))
        for r1 in range(-1, n-1):
            for r2 in range(r1, n-1):
                tot = min(tot, rc(0, r1, 0, m-1)+rc(r1+1, r2, 0, m-1) + rc(r2+1, n-1, 0, m-1))
        for c in range(-1, m-1):
            for r in range(-1, n-1):
                tot = min(tot, rc(0, r, 0, c) + rc(r+1, n-1, 0, c) + rc(0, n-1, c+1, m-1))
                tot = min(tot, rc(0, n-1, 0, c) + rc(0, r, c+1, m-1) + rc(r+1, n-1, c+1, m-1))
        for r in range(-1, n-1):
            for c in range(-1, m-1):
                tot = min(tot, rc(0, r, 0, c) + rc(0, r, c+1, m-1) + rc(r+1, n-1, 0, m-1))
                tot = min(tot, rc(0, r, 0, m-1) + rc(r+1, n-1, 0, c) + rc(r+1, n-1, c+1, m-1))
        return tot
