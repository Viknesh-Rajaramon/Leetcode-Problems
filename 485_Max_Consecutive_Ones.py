from imports import *

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev_count, curr_count = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_count += 1
            else:
                if prev_count < curr_count:
                    prev_count = curr_count
                curr_count = 0
        
        if prev_count < curr_count:
            return curr_count
        
        return prev_count
