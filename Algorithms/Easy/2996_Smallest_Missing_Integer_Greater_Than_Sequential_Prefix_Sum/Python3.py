from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        result, i = nums[0], 1
        while i < len(nums) and nums[i] == nums[i-1] + 1:
            result += nums[i]
            i += 1
            
        num_set = set(nums)
        while result in num_set:
            result += 1
        
        return result
