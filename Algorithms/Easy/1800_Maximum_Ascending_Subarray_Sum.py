from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_maxsum = nums[0]
        prev_maxsum = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                cur_maxsum += nums[i+1]
            else:
                if prev_maxsum < cur_maxsum:
                    prev_maxsum = cur_maxsum
                
                cur_maxsum = nums[i+1]
        
        if prev_maxsum < cur_maxsum:
            return cur_maxsum
        
        return prev_maxsum
