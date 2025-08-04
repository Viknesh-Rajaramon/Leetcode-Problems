from imports import *

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p, q = 0, 0

        if nums[0] >= nums[1]:
            return False
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return False
            elif p == 0 and i > 0 and nums[i] > nums[i + 1]:
                p = i
            elif p > 0 and q == 0 and i > p and nums[i] < nums[i + 1]:
                q = i
            elif q > 0 and nums[i] > nums[i + 1]:
                return False
        
        return bool(p and q and p < q)
