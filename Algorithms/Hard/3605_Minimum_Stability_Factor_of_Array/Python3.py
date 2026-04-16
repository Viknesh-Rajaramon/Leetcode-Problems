from typing import List
from math import gcd

class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)
        k = n.bit_length()
        st = [[0] * n for _ in range(k)]
        for j in range(n):
            st[0][j] = nums[j]
        
        for i in range(1, k):
            length, half = 1 << i, 1 << (i-1)
            for j in range(n-length+1):
                st[i][j] = gcd(st[i-1][j], st[i-1][j+half])
        
        def query_hcf(l: int, r: int) -> int:
            i = (r-l+1).bit_length() - 1
            return gcd(st[i][l], st[i][r+1-(1<<i)])
        
        def can_achieve(max_length: int) -> bool:
            if max_length+1 > n:
                return True
            
            moves, last_mod_idx = 0, -1
            for i in range(n-max_length):
                if i <= last_mod_idx:
                    continue
                
                if query_hcf(i, i+max_length) >= 2:
                    moves += 1
                    last_mod_idx = i+max_length
            
            return moves <= maxC
        
        result, low, high = n, 0, n
        while low <= high:
            mid = (low + high) // 2
            if can_achieve(mid):
                result, high = mid, mid - 1
            else:
                low = mid + 1
        
        return result
