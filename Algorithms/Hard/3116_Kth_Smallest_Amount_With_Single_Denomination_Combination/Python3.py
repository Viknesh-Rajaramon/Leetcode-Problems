from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        new_coins = []
        for i in range(len(coins)):
            for j in range(i):
                if coins[i] % coins[j] == 0:
                    break
            else:
                new_coins.append(coins[i])
        
        n = 1 << len(new_coins)
        lcm, left, right = [1] * n, k, new_coins[0]*k+1
        for mask in range(1, n):
            pre_mask = mask & (mask-1)
            i = (mask & -mask).bit_length()-1
            tmp = lcm[pre_mask] // gcd(lcm[pre_mask], new_coins[i])
            lcm[mask] = tmp*new_coins[i] if tmp <= right // new_coins[i] else right+1
        
        def get(x: int) -> int:
            count = 0
            for mask in range(1, n):
                if lcm[mask] > x:
                    continue
                
                if mask.bit_count() & 1:
                    count += x // lcm[mask]
                else:
                    count -= x // lcm[mask]
            
            return count
        
        while left < right:
            mid = (left+right) >> 1
            if get(mid) >= k:
                right = mid
            else:
                left = mid+1
        
        return left
