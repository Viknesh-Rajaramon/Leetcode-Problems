from typing import List

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        frequency, mod = [0] * 26, 10**9+7
        for c in s:
            frequency[ord(c) - ord("a")] += 1
        
        matrix = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for j in range(1, nums[i] + 1):
                matrix[(i+j) % 26][i] = 1
        
        def multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
            C = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(26):
                    for k in range(26):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
            
            return C

        def matrixExponentiation(matrix: List[List[int]], power: int) -> List[List[int]]:
            ans = [[0] * 26 for _ in range(26)]
            for i in range(26):
                ans[i][i] = 1
            
            x = matrix
            while power > 0:
                if power & 1:
                    ans = multiply(ans, x)
                
                x = multiply(x, x)
                power >>= 1
            
            return ans

        result, matrix = 0, matrixExponentiation(matrix, t)
        for i in range(26):
            for j in range(26):
                result = (result + matrix[i][j] * frequency[j]) % mod
            
        return result
