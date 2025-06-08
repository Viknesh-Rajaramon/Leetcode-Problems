from imports import *

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        good_sum = 0
        n = len(nums)
        for i in range(n):
            if i-k >= 0 and nums[i] <= nums[i-k]:
                continue
            
            if i+k < n and nums[i] <= nums[i+k]:
                continue
            
            good_sum += nums[i]
        
        return good_sum
