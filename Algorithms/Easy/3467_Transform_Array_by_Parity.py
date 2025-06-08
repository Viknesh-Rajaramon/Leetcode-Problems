from imports import *

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        num_even, num_odd = 0, 0
        for n in nums:
            if n % 2:
                num_odd += 1
            else:
                num_even += 1
        
        i = 0
        while num_even > 0:
            nums[i] = 0
            num_even -= 1
            i += 1
        
        while num_odd > 0:
            nums[i] = 1
            num_odd -= 1
            i += 1
        
        return nums
