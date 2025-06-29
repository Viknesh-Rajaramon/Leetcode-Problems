from imports import *

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n):
            result = (result + nums[i] * comb(n-1, i) % 10) % 10
        
        return result
