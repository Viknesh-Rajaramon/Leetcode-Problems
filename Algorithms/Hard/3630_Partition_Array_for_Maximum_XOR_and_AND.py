from typing import List
from itertools import combinations

class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        total_mask = (1 << 31) - 1
        result = 0

        def f(x: List[int]) -> int:
            b = []
            for v in x:
                for y in b:
                    v = min(v, v ^ y)
                
                if v:
                    b.append(v)
            
            b.sort(reverse = True)
            z = 0
            for y in b:
                z = max(z, z ^ y)

            return z

        for r in range(min(4, n) + 1):
            for c in combinations(range(n), r):
                and_val = 0 if not c else nums[c[0]]
                for i in c[1 : ]:
                    and_val &= nums[i]
                
                xor_val, t, s = 0, set(c), []
                for i in range(n):
                    if i not in t:
                        xor_val ^= nums[i]
                        s.append(nums[i])
                
                mask = (~xor_val) & total_mask
                s2 = [v & mask for v in s]
                y = f(s2) if s2 else 0
                result = max(result, xor_val + and_val + 2 * y)
        
        return result
