from typing import List

class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        def mul(a: List[int], b: List[int]) -> List[int]:
            result = [0, 0, 0, 0]
            result[0] = (a[0] * b[0] + a[1] * b[2]) % mod
            result[1] = (a[0] * b[1] + a[1] * b[3]) % mod
            result[2] = (a[2] * b[0] + a[3] * b[2]) % mod
            result[3] = (a[2] * b[1] + a[3] * b[3]) % mod
            return result
        
        result, m = [6, 0, 6, 0], [3, 2, 2, 2]
        n -= 1
        while n:
            if n & 1:
                result = mul(m, result)
            
            m = mul(m, m)
            n //= 2
            
        return sum(result) % mod
