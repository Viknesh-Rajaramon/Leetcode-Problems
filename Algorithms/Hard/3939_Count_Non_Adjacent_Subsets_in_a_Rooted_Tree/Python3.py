from typing import List

class Solution:
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        n, mod = len(parent), 10**9+7
        dp0, dp1 = [[0] * k for _ in range(n)], [[0] * k for _ in range(n)]
        for i in range(n):
            dp0[i][0], dp1[i][nums[i]%k] = 1, 1
        
        for i in range(n-1, 0, -1):
            p, new_dp0, new_dp1 = parent[i], [0] * k, [0] * k
            p_nz_0 = [r for r in range(k) if dp0[p][r] > 0]
            p_nz_1 = [r for r in range(k) if dp1[p][r] > 0]
            
            child_ways_any = [(dp0[i][r]+dp1[i][r]) % mod for r in range(k)]
            c_nz_any = [r for r in range(k) if child_ways_any[r] > 0]
            c_nz_0 = [r for r in range(k) if dp0[i][r] > 0]

            for r1 in p_nz_0:
                for r2 in c_nz_any:
                    idx = (r1 + r2) % k
                    new_dp0[idx] = (new_dp0[idx] + dp0[p][r1] * child_ways_any[r2]) % mod
                    
            for r1 in p_nz_1:
                for r2 in c_nz_0:
                    idx = (r1 + r2) % k
                    new_dp1[idx] = (new_dp1[idx] + dp1[p][r1] * dp0[i][r2]) % mod
                    
            dp0[p], dp1[p] = new_dp0, new_dp1
            
        return (dp0[0][0] + dp1[0][0] - 1) % mod
