from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        curr_inc, max_inc = 1, 0
        curr_dec, max_dec = 1, 0
        for i in range(n-1):
            if nums[i+1] > nums[i]:
                curr_inc += 1
            else:
                max_inc = max(max_inc, curr_inc)
                curr_inc = 1
            
            if nums[i+1] < nums[i]:
                curr_dec += 1
            else:
                max_dec = max(max_dec, curr_dec)
                curr_dec = 1
        
        return max(max_inc, curr_inc, max_dec, curr_dec)
