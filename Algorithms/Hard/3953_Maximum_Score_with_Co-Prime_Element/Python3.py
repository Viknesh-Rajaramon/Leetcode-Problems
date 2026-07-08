from typing import List
from functools import lru_cache

LIMIT = 100000
spf = list(range(LIMIT+1))
for i in range(4, LIMIT+1, 2):
    spf[i] = 2
for i in range(3, int(LIMIT**0.5)+1, 2):
    if spf[i] == i:
        for j in range(i*i, LIMIT+1, i*2):
            if spf[j] == j:
                spf[j] = i

class Solution:
    def maxScore(self, nums: List[int], maxVal: int) -> int:
        def get_primes(n: int) -> List[int]:
            primes = []
            while n > 1:
                primes.append(spf[n])
                n //= spf[n]
            
            return list(set(primes))
        
        @lru_cache(None)
        def get_subsets(n: int) -> List[int]:
            primes = get_primes(n)
            m = len(primes)
            subs = [0] * (1 << m)
            for i in range(1 << m):
                val = 1
                for j in range(m):
                    if i & (1 << j):
                        val *= primes[j]
                
                subs[i] = val
            
            return subs
        
        mx = max(max(nums), maxVal)+1
        freq = [0] * mx
        for x in nums:
            freq[x] += 1
        
        mults = freq.copy()
        for i in range(2, mx):
            for j in range(2*i, mx, i):
                mults[i] += freq[j]
        
        result = 1 if freq[1] > 0 else 0
        for i in range(mx-1, 1, -1):
            if result >= i:
                break
            
            subs = get_subsets(i)
            rem = -freq[i]
            for j in range(1, len(subs)):
                if j.bit_count() & 1:
                    rem += mults[subs[j]]
                else:
                    rem -= mults[subs[j]]
            
            if freq[i] > 0:
                cost = rem+freq[i]-1
                result = max(result, i-cost)
            elif i <= maxVal:
                cost = rem if rem > 0 else 1
                result = max(result, i-cost)

        return result
