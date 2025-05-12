from imports import *

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        i = 0
        total, result = 0, 0
        for j in range(len(nums)):
            total += nums[j]
            
            while i <= j and total * (j-i+1) >= k:
                total -= nums[i]
                i += 1
            
            result += j-i+1
        
        return result
