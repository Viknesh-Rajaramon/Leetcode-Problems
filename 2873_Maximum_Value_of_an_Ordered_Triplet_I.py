from imports import *

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        
        max_nums = [0] * n
        max_nums[-1] = nums[-1]
        for i in reversed(range(n-1)):
            max_nums[i] = max(nums[i], max_nums[i+1])

        left = nums[0]
        for j in range(1, n-1):
            if left <= nums[j]:
                left = nums[j]
                continue
                
            result = max(result, (left - nums[j]) * max_nums[j+1])
        
        return result
