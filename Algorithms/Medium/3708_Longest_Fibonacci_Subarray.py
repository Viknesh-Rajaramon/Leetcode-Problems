from imports import *

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result, n, curr = 2, len(nums), 2
        for i in range(2, n):
            if nums[i-1] + nums[i-2] == nums[i]:
                curr += 1
            else:
                curr = 2
            
            if curr > result:
                result = curr

        return result
