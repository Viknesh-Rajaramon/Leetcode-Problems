from imports import *

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        result = inf

        i, j = 0, len(nums) - 1
        while i < j:
            result = min(result, (nums[i] + nums[j]) / 2)
            i += 1
            j -= 1
        
        return result
