from imports import *

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        result = -1
        max_ = nums[n-1]
        for i in range(n-2, -1, -1):
            if nums[i] < max_:
                result = max(result, max_ - nums[i])
            else:
                max_ = nums[i]
        
        return result
