from imports import *

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        result = 0
        curr_sum, total_sum = 0, sum(nums)
        for i in range(len(nums)-1):
            curr_sum += nums[i]
            total_sum -= nums[i]
            
            if abs(total_sum - curr_sum) % 2 == 0:
                result += 1
        
        return result
