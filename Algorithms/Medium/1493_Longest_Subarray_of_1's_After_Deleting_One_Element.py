from imports import *

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) == 0:
            return 0
        
        n = len(nums)
        if sum(nums) == n:
            return n-1

        gaps = []
        for i in range(n):
            if nums[i] == 0:
                gaps.append(i)
        
        if len(gaps) == 1:
            return n-1
        
        result = gaps[1] - 1
        if len(gaps) > 2:
            for i in range(2, len(gaps)):
                result = max(result, gaps[i]-gaps[i-2]-2)
        
        if gaps[-1] < n-1:
            result = max(result, n-gaps[-2]-2)
            
        return result
