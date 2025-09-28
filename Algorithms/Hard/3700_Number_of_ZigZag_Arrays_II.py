from imports import *

MOD = 10**9 + 7

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        if n == 1:
            return m % MOD
        if n == 2:
            return (m * (m-1)) % MOD
        
        def matrix_mult(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
            n = len(A)
            res = [[0] * n for _ in range(n)]
            for i in range(n):
                for k in range(n):
                    if A[i][k]:
                        for j in range(n):
                            res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD
            
            return res
        
        def matrix_exp(mat: List[List[int]], power: int) -> List[List[int]]:
            n = len(mat)
            res = [[0] * n for _ in range(n)]
            for i in range(n):
                res[i][i] = 1
            
            base = mat
            while power > 0:
                if power & 1:
                    res = matrix_mult(res, base)
                
                base = matrix_mult(base, base)
                power >>= 1
            
            return res

        m = r - l + 1
        dp = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m-i, m):
                dp[i][j] = 1
        
        mat_exp = matrix_exp(dp, n-2)
        res = [0] * m
        for i in range(m):
            res[i] = sum(a*b for a, b in zip(mat_exp[i], list(range(m)))) % MOD
        
        return (2 * sum(res)) % MOD
