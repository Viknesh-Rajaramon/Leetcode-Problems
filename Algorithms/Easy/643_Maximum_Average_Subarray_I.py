from imports import *

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for i in range(len(nums) - k):
            curr_sum = curr_sum - nums[i] + nums[i+k]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum / k
