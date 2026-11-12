from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        result, inc, dec = 1, 1, 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                inc += 1
                dec = 1
            elif nums[i] > nums[i+1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            
            result = max(result, inc, dec)
        
        return result
