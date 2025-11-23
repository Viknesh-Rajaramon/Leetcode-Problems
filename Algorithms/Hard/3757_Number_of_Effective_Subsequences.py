from imports import *

class Solution:
    def countEffective(self, nums: List[int]) -> int:
        mod, total_or = 10**9 + 7, 0
        for num in nums:
            total_or |= num
            
        important_bits = []
        for b in range(20):
            if (total_or >> b) & 1:
                important_bits.append(b)

        k = len(important_bits)
        full_mask, freq = (1 << k) - 1, [0] * (1 << k)

        for num in nums:
            mask = 0
            for i, bit in enumerate(important_bits):
                if (num >> bit) & 1:
                    mask |= 1 << i
            
            freq[mask] += 1
        
        F = freq[:]
        for i in range(k):
            for mask in range(1 << k):
                if mask & (1 << i):
                    F[mask] += F[mask ^ (1 << i)]
        
        n = len(nums)
        pow_2 = [1] * (n+1)
        for i in range(1, n+1):
            pow_2[i] = pow_2[i-1] * 2 % mod
        
        result = 0
        for mask in range(1, 1 << k):
            if bin(mask).count("1") % 2 == 1:
                result = (result + pow_2[F[full_mask ^ mask]]) % mod
            else:
                result = (result - pow_2[F[full_mask ^ mask]]) % mod
        
        return result % mod
