from typing import List
from math import inf

class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:
        n = len(lists)
        total_masks = 1 << n
    
        length = [0] * total_masks
        median = [0] * total_masks
    
        for mask in range(1, total_masks):
            merged = []
            for i in range(n):
                if mask & (1 << i):
                    merged.extend(lists[i])
            
            merged.sort()
            length[mask] = len(merged)
            median[mask] = merged[(len(merged) - 1) // 2]
    
        dp = [inf] * total_masks
        for i in range(n):
            dp[1 << i] = 0
    
        for mask in range(1, total_masks):
            if dp[mask] == 0:
                continue
    
            first_bit = mask & -mask
            sub = (mask - 1) & mask
    
            while sub:
                if sub & first_bit:
                    other = mask ^ sub
                    cost = (
                        dp[sub]
                        + dp[other]
                        + length[sub]
                        + length[other]
                        + abs(median[sub] - median[other])
                    )
                    dp[mask] = min(dp[mask], cost)
                
                sub = (sub - 1) & mask
    
        return dp[total_masks - 1]
