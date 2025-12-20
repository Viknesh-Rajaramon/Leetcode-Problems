from typing import List

MOD = 10**9+7
L = 26

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        frequency = [0] * L

        for c in s:
            frequency[ord(c) - ord("a")] += 1
        
        matrix = [[0] * L for _ in range(L)]
        for i in range(L):
            for j in range(1, nums[i] + 1):
                matrix[(i+j) % L][i] = 1
        
        def multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
            C = [[0] * L for _ in range(L)]
            for i in range(L):
                for j in range(L):
                    for k in range(L):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            
            return C

        def matrixExponentiation(matrix: List[List[int]], power: int) -> List[List[int]]:
            ans = [[0] * L for _ in range(L)]
            for i in range(L):
                ans[i][i] = 1
            
            x = matrix
            while power > 0:
                if power & 1:
                    ans = multiply(ans, x)
                
                x = multiply(x, x)
                power >>= 1
            
            return ans

        matrix = matrixExponentiation(matrix, t)

        result = 0
        for i in range(L):
            for j in range(L):
                result = (result + matrix[i][j] * frequency[j]) % MOD
            
        return result
