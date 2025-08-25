from imports import *

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        result = []
        curr = 0

        n = len(nums)
        for i in range(n):
            curr = max(curr, nums[i])
            result.append(curr)
        
        curr = n-1
        for i in range(n-2, -1, -1):
            if result[i] > nums[curr]:
                result[i] = result[curr]
            
            if nums[i] < nums[curr]:
                curr = i
        
        return result
