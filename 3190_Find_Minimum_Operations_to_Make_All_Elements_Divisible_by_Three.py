from imports import *

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        min_ops = 0
        n = len(nums)
        for i in range(n):
            x = nums[i] % 3
            min_ops += min(x, 3 - x)
        
        return min_ops
