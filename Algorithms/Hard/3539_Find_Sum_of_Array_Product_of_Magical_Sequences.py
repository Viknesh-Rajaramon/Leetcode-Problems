from imports import *

MOD, MAX_ = 10**9 + 7, 31

FACT = [0] * MAX_
FACT[0] = 1
for i in range(1, MAX_):
    FACT[i] = FACT[i-1] * i % MOD

INVERSE_FACT = [0] * MAX_
INVERSE_FACT[-1] = pow(FACT[-1], -1, MOD)
for i in range(MAX_ - 1, 0, -1):
    INVERSE_FACT[i-1] = INVERSE_FACT[i] * i % MOD

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        power = [[1] * (m+1) for _ in range(n)]
        for i in range(n):
            for j in range(1, m+1):
                power[i][j] = power[i][j-1] * nums[i] % MOD
        
        @lru_cache(None)
        def dfs(i: int, left_m: int, x: int, left_k: int) -> int:
            c1 = x.bit_count()
            if c1 + left_m < left_k:
                return 0
            
            if i == n:
                return 1 if left_m == 0 and c1 == left_k else 0
            
            result = 0
            for j in range(left_m+1):
                bit = (x+j) & 1
                if bit <= left_k:
                    result += dfs(i+1, left_m-j, (x+j)>>1, left_k - bit) * power[i][j] * INVERSE_FACT[j]

            return result % MOD
        
        return dfs(0, m, 0, k) * FACT[m] % MOD
