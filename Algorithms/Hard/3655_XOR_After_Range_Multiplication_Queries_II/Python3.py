from typing import List
from collections import defaultdict

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD, n = 10**9 + 7, len(nums)
        B, groups, large = int(n**0.5) + 1, defaultdict(list), []
        for l, r, k, v in queries:
            if k <= B:
                groups[(k, l % k)].append((l, r, v))
            else:
                large.append((l, r, k, v))
        
        for (k, rem), qs in groups.items():
            m = (n-1-rem)//k + 1

            diff = [1] * (m+1)
            for l, r, v in qs:
                s, e = (l - rem) // k, (r - rem) // k
                diff[s] = (diff[s] * v) % MOD
                diff[e+1] = (diff[e+1] * pow(v, MOD-2, MOD)) % MOD
            
            curr, pos = 1, rem
            for t in range(m):
                curr = (curr * diff[t]) % MOD
                nums[pos] = (nums[pos] * curr) % MOD
                pos += k
            
        for l, r, k, v in large:
            for i in range(l, r+1, k):
                nums[i] = (nums[i] * v) % MOD
        
        result = 0
        for num in nums:
            result ^= num
        
        return result
