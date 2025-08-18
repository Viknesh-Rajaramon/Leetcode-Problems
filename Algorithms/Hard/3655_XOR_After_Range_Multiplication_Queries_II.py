from imports import *

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        B = int(n**0.5) + 1
        
        groups, large = defaultdict(list), []
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
            i = l
            while i <= r:
                nums[i] = (nums[i] * v) % MOD
                i += k
        
        result = 0
        for num in nums:
            result ^= num
        
        return result
