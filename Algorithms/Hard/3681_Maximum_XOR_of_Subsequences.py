from typing import List

class Solution:
    def maxXorSubsequences(self, nums: List[int]) -> int:
        max_bits = 31
        basis = [0] * max_bits
        for num in nums:
            x = num
            for b in range(max_bits - 1, -1, -1):
                if not (x >> b) & 1:
                    continue
                
                if basis[b]:
                    x ^= basis[b]
                else:
                    basis[b] = x
                    break
        
        result = 0
        for b in range(max_bits - 1, -1, -1):
            if (result ^ basis[b]) > result:
                result ^= basis[b]
        
        return result
