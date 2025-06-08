from imports import *

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_abs_diff = abs(nums[0] - nums[n-1])
        for i in range(n-1):
            max_abs_diff = max(max_abs_diff, abs(nums[i] - nums[i+1]))
        
        return max_abs_diff
