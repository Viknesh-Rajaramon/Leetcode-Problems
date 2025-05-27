from imports import *

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        num_even = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] % 2 == 0:
                num_even += 1
            
            if num_even > 1:
                return True
        
        return False
