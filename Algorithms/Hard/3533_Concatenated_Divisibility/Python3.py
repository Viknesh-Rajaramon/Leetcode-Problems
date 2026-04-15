from typing import List
from functools import cache

class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums.sort()
        result = []
        
        @cache
        def dp(mask, r):
            if mask == (1 << n) - 1:
                return r == 0
            
            for i in range(n):
                if (1 << i) & mask:
                    continue
                
                result.append(nums[i])
                if dp(mask | (1 << i), int(str(r) + str(nums[i])) % k):
                    return True
                
                result.pop()
            
            return False

        dp(0, 0)
        return result
