from typing import List
from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq, count = [0] * (mx+1), [0] * (mx+1)
        for num in nums:
            freq[num] += 1
        
        for g in range(mx, 0, -1):
            total = 0
            for m in range(g, mx+1, g):
                total += freq[m]
            
            pairs = total*(total-1)//2
            for m in range(2*g, mx+1, g):
                pairs -= count[m]
            
            count[g] = pairs
        
        pref, vals, s = [], [], 0
        for g in range(1, mx+1):
            if not count[g]:
                continue
            
            s += count[g]
            pref.append(s)
            vals.append(g)
        
        result = []
        for q in queries:
            pos = bisect_left(pref, q+1)
            result.append(vals[pos])

        return result
